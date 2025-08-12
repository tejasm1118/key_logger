# Keylogger Lab (Educational Cybersecurity Project)

## ⚠️ Disclaimer
This project is for **educational use only**.  
Do **NOT** use this tool on any system without explicit permission from the owner.  
Unauthorized use of keyloggers is illegal and unethical.

---

## 📌 Overview
This lab demonstrates:
- How a simple user-level keylogger works in Python.
- How detection scripts can spot suspicious processes.
- The importance of endpoint security in defending against such threats.

It is designed to run **only in a safe, local lab environment** such as a sandbox or virtual machine.

---

## 🛠 Features
- **Keylogger** using `pynput` to capture keystrokes.
- **Detector** using `psutil` to find suspicious running processes.
- **Demo runner** to simulate both attack and detection in one session.
- Auto-creation of log directory and timestamped keystroke logging.

## Security Lessons
- **Input interception is easy at the user level.
- **Detection tools must monitor active processes and hooks.
- **Logging keystrokes without consent is illegal; security teams must defend against this.



