import os
import datetime
import webbrowser
import pywhatkit as kit
import pyjokes
import pyautogui
import sched
import time
import ctypes

from head.mouth import speak
from head.ear import listen
from head.brain import brain

from features.welcome import welcome
from features.location import get_location
from features.fetch_weather import fetch_weather
from features.news import news
from features.ip_address import get_ip_address
from features.increase_brightness import increase_brightness
from features.decrease_brightness import decrease_brightness
from features.increase_volume import increase_volume
from features.decrease_volume import decrease_volume
from features.battery_status import battery_status

scheduler = sched.scheduler(time.time, time.sleep)

def take_command():
    """Take user input and covert them to text"""
    return listen()

def handle_commands(query):
    if "what is my ip" in query or "my ip address" in query or "ip address" in query:
        get_ip_address()
    elif "where am i" in query or "my current location" in query or "current location" in query:
        city = get_location()
        speak(f"You are currently in {city}.")
        print(f"You are currently in {city}.")
    elif "weather" in query or "weather forecast" in query or "current weather" in query or "weather report" in query:
        city = get_location()
        if city:
            fetch_weather(city)
    elif "tell me some jokes" in query or "tell me a joke" in query or "joke" in query:
        joke = pyjokes.get_joke()
        speak(joke)
    elif "open notepad" in query:
        speak("Opening Notepad")
        os.startfile("C:\\Windows\\notepad.exe")
    elif "open command prompt" in query:
        speak("Opening Command Prompt")
        os.system("start cmd")
    elif "opencalculator" in query:
        speak("Opening Calculator")
        os.startfile("C:\\Windows\\System32\\calc.exe")
    elif "open instagram" in query:
        speak("Opening Instagram")
        webbrowser.open("https://www.instagram.com")
    elif "open whatsapp" in query:
        speak("Opening WhatsApp")
        webbrowser.open("https://web.whatsapp.com")
    elif "open browser" in query or "open brave" in query:
        os.startfile("C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe")
    elif "open google" in query or "search on google" in query:
        speak("What should I search on Google?")
        search_query = take_command()
        if search_query:
            webbrowser.open(f"https://www.google.com/search?q={search_query}")
    elif "open youtube" in query or "youtube" in query:
        webbrowser.open("https://www.youtube.com")
    elif "open linkedin" in query:
        webbrowser.open("https://www.linkedin.com")
    elif "open facebook" in query:
        webbrowser.open("https://www.facebook.com")
    elif "open reddit" in query:
        webbrowser.open("https://www.reddit.com")
    elif "open github" in query:
        webbrowser.open("https://www.github.com/Mohit-480")
    elif "open my github repository" in query or "github repository" in query:
        webbrowser.open("https://github.com/Mohit-480?tab=repositories")
    elif "open" in query:
        query = query.replace("open", "").strip()
        pyautogui.press("super")
        pyautogui.typewrite(query)
        pyautogui.press("enter")
    elif query.startswith("play ") or query.startswith("bajao "):
        song = query.split(' ', 1)[1]
        speak(f'Playing {song}')
        kit.playonyt(song)
    elif "news" in query or "current news" in query:
        news()
    elif "increase brightness" in query or "turn up brightness" in query or "increase the brightness" in query:
        new_brightness = increase_brightness()
        if new_brightness is not None:
            speak(f"Brightness increased to {new_brightness}%.")
    elif "decrease brightness" in query or "turn down brightness" in query or "decrease the brightness" in query:
        new_brightness = decrease_brightness()
        if new_brightness is not None:
            speak(f"Brightness decreased to {new_brightness}%.")
    elif "increase volume" in query or "turn up volume" in query or "increase the volume" in query:
        new_volume = increase_volume()
        if new_volume is not None:
            speak(f"Volume increased to {new_volume}%.")
    elif "decrease volume" in query or "turn down volume" in query or "decrease the volume" in query:
        new_volume = decrease_volume()
        if new_volume is not None:
            speak(f"Volume decreased to {new_volume}%.")
    elif "what is the time" in query or "current time" in query:
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        speak(f"The current time is {current_time}.")
    elif "what is the date" in query or "today's date" in query or "current date" in query or "tell me the current date" in query:
        current_date = datetime.datetime.now().strftime("%A, %B %d, %Y")
        speak(f"Today is {current_date}.")
    elif "battery status" in query or "battery" in query:
        status = battery_status()
        speak(status)
    elif "exit" in query or "goodbye" in query or "stop" in query or "close yourself" in query or "bye" in query or "see you later" in query:
        speak("Goodbye! Have a nice day.")
        exit()
    elif "shutdown system" in query:
        os.system("shutdown /s /t 1")
        exit()
    elif "restart system" in query:
        os.system("shutdown /r /t 1")
        exit()
    elif "lock system" in query or "lock my computer" in query:
        speak("Locking the system.")
        ctypes.windll.user32.LockWorkStation()
    elif "sign out" in query or "log off" in query:
        speak("Signing you out. Please wait.")
        os.system("shutdown /l")
        exit()
    else:
        brain(query)

def xolo():
    welcome()
    while True:
        query = take_command().strip()
        if query:
            handle_commands(query)
        scheduler.run(blocking=False)

if __name__ == "__main__":
    xolo()
