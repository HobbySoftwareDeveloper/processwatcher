### copyright (c) HobbySoftwareDeveloper 2024
### source code

import psutil

def chkproc(processName):
    for proc in psutil.process_iter():
        try:
            if processName.lower() in proc.name().lower():
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return False

while chkproc("main") == True:
    pass

else: 

    print("process has been terminated")
    input("")

