import time
import subprocess

seconds = 0
minutes = 0
hours = 0
days = 0

while True:
    seconds = seconds + 1

    if seconds == 59:
        minutes = minutes + 1
        seconds = 0

    if minutes == 59:
        minutes = 0
        hours = hours + 1

    if hours == 24:
        hours = 0
        days = days +1

    time.sleep(1)
    subprocess.call("cls",shell=True)
    print(str(days)+":"+str(hours)+":"+str(minutes)+":"+str(seconds))

