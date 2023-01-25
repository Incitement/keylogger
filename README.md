# Basic Python Keylogger

Hello, welcome! This repo is a simple keylogger script written in Python that I have used to learn more about Python and general security principles. For right now this is a heavy work in progress, and is only in a concept state at this point in time. The keylogger works for both Windows and Linux platforms.

**Disclaimer: The software found in this repository is for research and learning purposes only, and should only be used on systems that you have proper authorization to perform malicious actions on. Do not use this for any malicious purposes or intents.**

## Usage
After moving to the directory that you download the repo into, just call the logger with:
```
python logger.py
```
and the logger will begin to listen for keystrokes. You should see your keystroke display in the terminal.

The keystrokes are also stored in the log file stated in the beginning of the logger.py file, in the default case "log.txt". With the current implementation, the keystroke logging is not exactly elegant, and may cause abnormal disk usage.
