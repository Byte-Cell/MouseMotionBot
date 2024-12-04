import pyautogui
import time
import random

def move_mouse():
    screenWidth, screenHeight = pyautogui.size()
    x = random.randint(0, screenWidth)
    y = random.randint(0, screenHeight)
    pyautogui.moveTo(x, y, duration=0.5)

while True:
    move_mouse()
    time.sleep(60)
    print('i am now moving')
    


