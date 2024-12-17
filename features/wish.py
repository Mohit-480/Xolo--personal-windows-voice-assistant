from datetime import datetime, date
from head.mouth import speak
from Data.dialogue_data.wish_dlg import *
import random

now = datetime.now()
current_hour = now.hour
today = now.strftime("%A")  # Get the day name
formatted_date = now.strftime("%d %b, %Y")  # Get the date in 'dd Mon, yyyy' format

def wish():
    # Time-based greetings
    if 5<= current_hour < 12:
        gm_dlg = random.choice(good_morning_dlg)
        speak(gm_dlg)
    elif 12 <= current_hour < 17:
        ga_dlg = random.choice(good_afternoon_dlg)
        speak(ga_dlg)
    elif 17<= current_hour < 21:
        ge_dlg = random.choice(good_evening_dlg)
        speak(ge_dlg)
    else:
        gn_dlg=random.choice(good_night_dlg)
        speak(gn_dlg)

