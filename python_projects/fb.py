import pyautogui

import time
i = 0

while(i <= 500):
    time.sleep(0.5)
    msg = f"I Love You :) && Happy Valentines Day :-*"
    pyautogui.typewrite(msg)

    time.sleep(0.5)
    pyautogui.press('enter')
    i=i+1
