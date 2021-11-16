import pyttsx3
import datetime
import time
import speech_recognition as sr
import python_weather

import testing

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

miaProtocol = {"location": False, "basic_info": True, "time": [8, 12], "goverment": True, "adds": True}
unknown_Protocol={}

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def authenticate():
    speak("Who are you?")
    query = takeCommand().lower()

    if query == "Mia":
        speak("Hello" + query)
        time = get_Time(miaProtocol)
        if time == True:
            takeAction(miaProtocol)
    else:
        time = get_Time(unknown_Protocol)
        if time == True:
            takeAction(unknown_Protocol)

def register_protocol():
    unknown_Protocol[0] = {"morning": testing.morning_input}
    unknown_Protocol[1] = {"night": testing.night_input}
    unknown_Protocol[2] = {"adds": testing.a_state}
    unknown_Protocol[3] = {"location": testing.l_state}

def takeAction(protocol):
    speak("What can i do for you?")

    query = takeCommand().lower()

    if query == "time":
        time(protocol)
    elif query == "date":
        day(protocol)
    elif query == "joke":
        jokes(protocol)


def takeCommand():
    rec = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        rec.pause_threshold = 1
        rec.adjust_for_ambient_noise(source)
        audio = rec.listen(source)

    try:
        print("Recognizing...")
        query = rec.recognize_google(audio, language='en-US')
        print(f"user said: {query} \n")
        
    except Exception as ex:
        print(ex)
        print("unable to recognize your voice")
        return "None"
    
    return query


def get_Time(protocol):
    time_Allowed = False
    hour = int(datetime.datetime.now().hour)
    if protocol["time"[0]] < hour:
        speak("Sorry you havn't allowed me to listen to you yet")
        time_Allowed = False

    elif protocol["time"[1]] > hour:
        speak("Sorry you haven't allowed my to listen further")
        time_Allowed = False

    else:
        strTime = datetime.datetime.now().strftime("%H%M%S")
        speak(f"The time is {strTime}")
        time_Allowed = True

    return time_Allowed

def day(protocol):
    if protocol["basic_info"] == True:
        day = datetime.datetime.today().weekday() + 1
        strDate = datetime.date.today()
        
        Day_dict = {1: 'Monday', 2: 'Tuesday', 3: 'Wednesday',
                    4: 'Thursday', 5: 'Friday', 6: 'Saturday',
                    7: 'Sunday'}
        
        if day in Day_dict.keys():
            day_of_the_week = Day_dict[day]
            print(day_of_the_week)
            speak("The day is " + day_of_the_week)
            speak(f"{strDate}")
    else:
        speak("Sorry you have not allowed this")

def weather(protocol):
    client = python_weather.Client(format=python_weather.IMPERIAL)
    weather = client.find("Copenhagen")

