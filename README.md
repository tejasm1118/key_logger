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

---

## 📂 Project Structure
keylogger-lab/
│
├── README.md # Project documentation
├── requirements.txt # Dependencies
├── .gitignore # Ignores logs and other local files
│
├── src/
│ ├── keylogger.py # Educational keylogger
│ ├── detector.py # Process detection script
│ └── demo_runner.py # Runs keylogger + detector together
│
└── logs/ # Keystroke logs (not tracked in Git)
