import random
from Data.dialogue_data.welcome_dlg import *
from head.mouth import speak

def welcome():
    welcome_d = random.choice(welcome_dlg)
    speak(welcome_d)
