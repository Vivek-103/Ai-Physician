import speech_recognition as sr
import pyttsx3
from PIL import Image

def listen_to_user():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
    try:
        return recognizer.recognize_google(audio)
    except sr.UnknownValueError:
        return "Sorry, I didn't catch that."

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
