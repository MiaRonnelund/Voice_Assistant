import pyttsx3
import datetime
import time
import speech_recognition as sr
import python_weather
import asyncio

import protocol_Window

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

miaProtocol = {"time": [8, 19], "adds": True, "location": False}
unknown_Protocol={}

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def authenticate():
    speak("Who are you?")
    query = takeCommand().lower()

    if query == "mia":
        speak("Hello" + query)
        allowed = allowedToListen(miaProtocol)
        if allowed == True:
            takeAction(miaProtocol)
    else:
        register_protocol()
        allowed = allowedToListen(unknown_Protocol)
        if allowed == True:
            takeAction(unknown_Protocol)

def register_protocol():
    protocol = protocol_Window.pInput()
    unknown_Protocol["time"] = [protocol[0], protocol[1]]
    unknown_Protocol["adds"] = protocol[2]
    unknown_Protocol["location"] = protocol[3]

def takeAction(protocol):
    speak("What can i do for you?")
    query = takeCommand().lower()

    while True:
        if query == "time":
            get_Time()
        elif query == "weather":
            loop = asyncio.get_event_loop()
            loop.run_until_complete(weather(protocol))
        elif query == "order":
            add(protocol)


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


def allowedToListen(protocol):
    listen_Allowed = False
    hour = int(datetime.datetime.now().hour)
    if protocol["time"][0] > hour:
        speak("Sorry you havn't allowed me to listen to you yet")
        listen_Allowed = False

    elif protocol["time"][1] < hour:
        speak("Sorry you haven't allowed my to listen further")
        listen_Allowed = False

    else:
        listen_Allowed = True

    return listen_Allowed

def get_Time():
    strTime = datetime.datetime.now().strftime("%H%M%S")
    speak(f"The time is {strTime}")

async def weather(protocol):
    if protocol["location"] == True:
        client = python_weather.Client()
        weather = await client.find("Copenhagen")
        speak(weather.current.temperature)

        await client.close()
    
    else:
        speak("Sorry you location is disabled")

def add(protocol):
    if protocol["adds"] == True:
        speak("What would you like to order?")
        query = takeCommand()

        speak(f"Ordering {query}")