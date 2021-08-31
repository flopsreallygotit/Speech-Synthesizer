#Author: flopsreallygotit
#Python 3

import SpeechRecognition as sr
import os
import pyttsx3

def Speech_Recognition():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("--> Say Something: ")
        audio = recognizer.listen(source)
    try:
        speech = recognizer.recognize_google(audio, language="en-EN")
    except:
        speech = "Error"

    return speech

def Speech_Insonation(speech):
    tts = pyttsx3.init()
    tts.say(speech)

    tts.runAndWait()
    
while True:
    Speech_Insonation(Speech_Recognition())   