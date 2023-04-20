import pyautogui
import time

with open('input.txt', encoding='utf8') as file:
    content = file.readlines()

print("you have 25 seconds before the app starts running")
time.sleep(25)

for item in content:
    pyautogui.typewrite(item)
    time.sleep(1)