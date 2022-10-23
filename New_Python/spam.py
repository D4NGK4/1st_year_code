from os import sched_setscheduler
import pyautogui as pyat
import time

message = 10

time.sleep(10)
while message > 0:   
    pyat.typewrite("I Love You")
    time.sleep(0.5)
    pyat.press('enter')
    message -= 1
    
