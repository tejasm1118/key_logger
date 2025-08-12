import subprocess
import time
import os

if __name__ == "__main__":
    keylogger = subprocess.Popen(["python", "keylogger.py"])
    print("[*] Keylogger started in background...")

    time.sleep(5)  # Give time to "type" something in lab
    print("[*] Running detector...")
    subprocess.call(["python", "detector.py"])

    print("[*] Stopping keylogger...")
    keylogger.terminate()
