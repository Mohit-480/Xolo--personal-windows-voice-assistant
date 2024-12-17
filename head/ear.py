import speech_recognition as sr
import os
from mtranslate import translate
from colorama import Fore, Style, init

init(autoreset=True)

def clear_console():
    """Clear the console for a clean output."""
    os.system("cls" if os.name == "nt" else "clear")

def display_message(message, color=Fore.WHITE):
    """Display a message in the specified color without clearing."""
    print(color + message + Style.RESET_ALL)

def Trans_hindi_to_english(txt):
    """Translate text from Hindi to English."""
    return translate(txt, "en-in", "hi")

def listen():
    """Main function to listen to audio and recognize speech."""
    recognizer = sr.Recognizer()
    recognizer.dynamic_energy_threshold = False
    recognizer.energy_threshold = 2500  # Adjust based on environment

    recognizer.pause_threshold = 0.5
    recognizer.non_speaking_duration = 0.2

    with sr.Microphone() as source:
        display_message("I am listening...", Fore.LIGHTYELLOW_EX)
        recognizer.adjust_for_ambient_noise(source, duration=1)

        try:
            audio = recognizer.listen(source, timeout=5)
            display_message("Now recognizing...", Fore.LIGHTBLUE_EX)

            recognized_txt = recognizer.recognize_google(audio).lower()

            if recognized_txt:
                translated_txt = Trans_hindi_to_english(recognized_txt)
                clear_console()
                display_message(f"XOLO: {translated_txt}", Fore.GREEN)
                return translated_txt
            else:
                return ""

        except sr.UnknownValueError:
            # Simply return None on unknown speech without prompting user
            return ""
        except sr.WaitTimeoutError:
            # Skip timeout prompt and return empty response silently
            return ""
        except Exception as e:
            display_message(f"An error occurred: {str(e)}", Fore.RED)
            return ""
