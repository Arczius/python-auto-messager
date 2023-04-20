import os

packages = [
    'pyautogui'
]

for package in packages:
    os.system('pip install ' + package)