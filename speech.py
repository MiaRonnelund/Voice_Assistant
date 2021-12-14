import pyttsx3
import datetime
import time
import speech_recognition as sr
import python_weather
import asyncio


engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

miaPolicy = {"time": [8, 19], "advertisement": True, "location": False}
unknown_Policy={}

#Uses pyttsx3 to convert text to speech
def speak(text):
    engine.say(text)
    engine.runAndWait()

#Take user audio and convert til text
#Returns the query (the user input)
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

#Authenticate the speaker
def authenticate():
    speak("Who are you?")
    query = takeCommand().lower()

    if query == "mia":
        speak("Hello" + query)
        allowed = allowedToListen(miaPolicy)
        if allowed == True:
            takeAction(miaPolicy)
    else:
        register_protocol()
        allowed = allowedToListen(unknown_Policy)
        if allowed == True:
            takeAction(unknown_Policy)

#register protocol by input()
def register_protocol():
    speak("Please define your privacy protocol")

    #Set time for allowed listen
    speak("When am I allowed to start listening?")
    morning = int(input("Please type whole number between 0 - 24: \n"))

    speak("When should i stop listening?")
    night = int(input("Please type whole number between 0 - 24: \n"))

    unknown_Policy["time"] = [morning, night]

    #Set adds
    speak("Would you allow adds?")
    advertisement = input("Please type 'yes' or 'no'\n").lower()
    if(advertisement == "yes" ):
        unknown_Policy["advertisement"] = True
    else:
        unknown_Policy["advertisement"] = False

    #Set location
    speak("Would you allow location?")
    location = input("Please type 'yes' or 'no' \n").lower()
    if(location == "yes"):
        unknown_Policy["location"] = True
    else:
        unknown_Policy["location"] = False

    print(unknown_Policy)

#Call different functions based on query
def takeAction(policy):
    speak("What can i do for you?")
    current = time.time()

    while True:
        query = takeCommand().lower()
        if "time" in query:
            get_Time()
        elif "weather" in query:
            if(policy["location"]==True):
                loop = asyncio.get_event_loop()
                loop.run_until_complete(weather())
            else:
                speak("Sorry you location is disabled")
        elif "order" in query:
            if(policy["advertisement"]==True):
                order()
            else:
                speak("Sorry, adds is disabled. I can't run this command")


#Checks that the current time is within range of the given time preferences
def allowedToListen(policy):
    listen_Allowed = False
    hour = int(datetime.datetime.now().hour)
    if policy["time"][0] > hour:
        speak("Sorry you havn't allowed me to listen to you yet")
        listen_Allowed = False

    elif policy["time"][1] <= hour:
        speak("Sorry you haven't allowed my to listen further")
        listen_Allowed = False

    else:
        listen_Allowed = True

    return listen_Allowed

#If query is time this function is called
#Speaks the current time
def get_Time():
    strTime = datetime.datetime.now().strftime("%H%M%S")
    speak(f"The time is {strTime}")

#Query == Weather
#speaks the current temperature of Copenhagen - if 'location' allowed
async def weather():
    client = python_weather.Client()
    weather = await client.find("Copenhagen")
    temp = weather.current.temperature
    speak(f"It is {temp} degrees celcius in Copenhagen today")

    await client.close()

#Query == order
#speaks food order if 'adds' allowed
def order():
    speak("What would you like to order?")
    query = takeCommand()

    speak(f"Ordering {query}")