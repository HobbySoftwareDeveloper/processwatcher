#process watcher execute program

### copyright (c) HobbySoftwareDeveloper 2023-2024
### source code

import os 
import sys
import time

def resource_path(relative_path):

    try:
        base_path = sys._MEIPASS

    except Exception:
        
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

os.startfile(resource_path("watcher.exe"))

time.sleep(1)

import psutil

def chkproc(processName):
    for proc in psutil.process_iter():
        try:
            if processName.lower() in proc.name().lower():
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return False

while chkproc("watcher") == True:
    pass

else: 

    print("process has been terminated")
    input("")

