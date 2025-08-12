import psutil

def detect_keylogger():
    suspicious = []
    for proc in psutil.process_iter(['pid', 'name', 'cmdline']):
        try:
            cmdline = ' '.join(proc.info['cmdline']) if proc.info['cmdline'] else ''
            if 'pynput' in cmdline or 'keylogger.py' in cmdline:
                suspicious.append(proc.info)
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            pass
    return suspicious

if __name__ == "__main__":
    found = detect_keylogger()
    if found:
        print("[!] Suspicious keylogger processes detected:")
        for p in found:
            print(f"    PID: {p['pid']}, Name: {p['name']}, Cmd: {p['cmdline']}")
    else:
        print("[OK] No keylogger process detected.")
