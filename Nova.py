import os
import random
from datetime import datetime

def speak(text):
    os.system(f'termux-tts-speak "{text}"')

def listen():
    speak("I'm listening...")
    os.system("termux-speech-to-text > ~/speech.txt")
    try:
        with open(os.path.expanduser("~/speech.txt"), "r") as file:
            return file.read().strip().lower()
    except:
        return ""

def greet():
    hour = datetime.now().hour
    if 0 <= hour < 12:
        speak("Good morning!")
    elif 12 <= hour < 17:
        speak("Good afternoon!")
    elif 17 <= hour < 20:
        speak("Good evening!")
    else:
        speak("Good night!")

def farewell():
    responses = ["Goodbye!", "See you later!", "Take care!", "Bye for now!"]
    speak(random.choice(responses))

def open_app(app_name):
    apps = {
        "settings": "am start -a android.settings.SETTINGS",
        "camera": "am start -a android.media.action.IMAGE_CAPTURE",
        "whatsapp": "monkey -p com.whatsapp -c android.intent.category.LAUNCHER 1",
        "telegram": "monkey -p org.telegram.messenger -c android.intent.category.LAUNCHER 1",
        "mi music": "monkey -p com.miui.player -c android.intent.category.LAUNCHER 1",
        "youtube": "monkey -p com.google.android.youtube -c android.intent.category.LAUNCHER 1",
    }
    cmd = apps.get(app_name)
    if cmd:
        os.system(cmd)
        speak(f"Opening {app_name}")
    else:
        speak(f"Sorry, I don't know how to open {app_name}")

# Start the assistant
greet()

while True:
    query = listen()

    if not query:
        continue

    if "hello" in query or "hi" in query:
        speak("Hello! How can I help you?")
    elif "how are you" in query:
        speak("I'm doing great, thanks for asking!")
    elif "your name" in query:
        speak("I am your voice assistant.")
    elif "time" in query:
        now = datetime.now().strftime("%H:%M")
        speak(f"The time is {now}")
    elif "play music" in query or "open mi music" in query:
        open_app("mi music")
    elif "open youtube" in query:
        open_app("youtube")
    elif "open whatsapp" in query:
        open_app("whatsapp")
    elif "open camera" in query:
        open_app("camera")
    elif "open settings" in query:
        open_app("settings")
    elif "bye" in query or "exit" in query or "quit" in query:
        farewell()
        break
    else:
        speak("Sorry, I didn't understand that.")
