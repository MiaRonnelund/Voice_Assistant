from __future__ import print_function
import random
import time

import speech_recognition as sp

def recognize_speech(recognizer, microphone):
    if not isinstance(recognizer, sp.Recognizer):
        raise TypeError("regonizer needs to be Recognizer")
    
    if not isinstance(microphone, sp.Microphone):
        raise TypeError("microphone needs to be of instance 'microphone'")
    
    with microphone as source:
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    response = {
        "success": True,
        "error": None,
        "transcription": None
    }

    try:
        response["transcription"] = recognizer.recognize_google(audio)
    except sp.RequestError:
        response["success"] = False
        response["error"] = "API unavailable"
    except sp.UnknownValueError:
        response["error"] = "Uable to recognize speech"
    return response


if __name__ == "__main__":
    WORDS = ["plane", "car", "banana", "drink", "phone"]
    GUESSES = 4
    LIMIT = 5

    recognizer = sp.Recognizer()
    microphone = sp.Microphone()

    word = random.choice(WORDS)

    intructions = (
        "I'm thinking of a word \n"
        "{words} \n"
        "you have {n} tries to guess the correct word"
    ).format(words = ", ".join(WORDS), n=GUESSES)

    print(intructions)
    time.sleep(3)


    for i in range(GUESSES):
        for j in range(LIMIT):
            print("{}. guess: speak!".format(i+1))
            guess = recognize_speech(recognizer, microphone)
            if guess["transcription"]:
                break
            if not guess["success"]:
                break
            print("I didn't catch that, can you repeat?")

        if guess["error"]:
            print("ERROR: {}".format(guess["error"]))
            break

        print("you said {}".format(guess["transcription"]))

        correct_guess = guess["transcription"].lower() == word.lower()
        more_attempts = i < GUESSES - 1

        if correct_guess:
            print("correct! you win")
            break
        elif more_attempts:
            print("Wrong, try again")
        else:
            print("sorry, you loose! \nI was thinking of '{}'".format(word))
            break


