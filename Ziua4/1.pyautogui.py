# Mutam cursorul random

import pyautogui
import random
import time

dimensiuni = pyautogui.size()
print(dimensiuni, type(dimensiuni))

height = dimensiuni.height
width = dimensiuni.width

print(height)
print(width)

start_time = time.time()
duration = 20 #secunde

while time.time() - start_time < duration:
    random_height = random.randint(0, height)
    random_width= random.randint(0, width)
    print(f"Cursorul se va muta la {random_height} X {random_width}")
    pyautogui.moveTo(random_width, random_height, duration=1) #duration = cat dureaza miscarea => va interpola pozitiile intermediare
    time.sleep(2)

