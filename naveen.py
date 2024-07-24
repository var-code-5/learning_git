import pyautogui
import keyboard
import time

# 1371,951

time.sleep(5)

comments = ["!points","!volter","!top"]

while True:
    for i in comments:
        pyautogui.click(1371,951)
        keyboard.write(i)
        time.sleep(0.5)
        keyboard.press_and_release('enter')
        time.sleep(0.5)