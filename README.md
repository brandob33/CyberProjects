# CyberProjects 🛡️

A collection of cybersecurity tools and scripts for educational purposes. Developed by a CS student with intention to learn and dive deeper into cybersecurity projects.

## Projects

### 1. Keyloggers

This directory contains two types of keyloggers developed in Python.

#### File Logger (`filelogger.py`)
A basic keylogger that captures keystrokes and saves them to a local `log.txt` file.
- **Features**: Captures all keys, handles special keys.
- **Usage**: Run `python filelogger.py`.

#### Webhook Logger (`webhooklogger.py`)
An advanced keylogger that sends captured keystrokes to a Discord Webhook. It is designed to be compiled into a standalone `.exe` for stealth execution.
- **Features**: 
    - Sends logs to Discord.
    - Runs in the background (stealth mode).
    - Can be compiled to `.exe`.
    - Auto-startup via Registry persistence.

---

## Getting Started

### Prerequisites
- Python 3.x
- `pip install pyinstaller` (for building .exe)

### Configuration

#### Local Testing
1.  Add your webhook to `Keyloggers/Webhook/webhooklogger.py`.
2.  Run `python webhooklogger.py`.


#### Building the Executable (Standalone)
To build a standalone `.exe` that works on any machine without Python:
1.  Edit `Keyloggers/Webhook/webhooklogger.py` and replace the `WEBHOOK_URL` variable with your actual URL string.
2.  Run the build command:
    ```powershell
    pyinstaller --onefile --noconsole --name "Keylogger" webhooklogger.py
    ```
3.  The output file will be in the `dist` folder.

> **Note**: For a more organized build, use:
> `pyinstaller --onefile --noconsole --name "Keylogger" --distpath "./build/dist" --workpath "./build/temp" --specpath "./build" webhooklogger.py`

---

##  Disclaimer

**This project is for educational purposes only.** 
The author is not responsible for any misuse of this software. Using keyloggers on computers you do not own or have permission to access is illegal and unethical. Ensure you have explicit consent before running these scripts on any system.
