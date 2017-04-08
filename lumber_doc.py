#
#  LumberDoctor
# ========================================
# [] File Name : lumber_doc.py
#
# [] Creation Date : 4/8/2017
#
# [] Created By : Ali Gholami (aligholami7596@gmail.com)
# ========================================
#

import pyautogui
import time

# Wait until the game runs
time.sleep(5)

image = pyautogui.screenshot()

right_critical_pixel = image.getpixel((826, 418))
left_critical_pixel = image.getpixel((710, 418))

person_head = image.getpixel((826, 427))

tree_color = (161, 116, 56)
back_color = (211, 247, 255)

while True:
    time.sleep(0.15)
    image = pyautogui.screenshot()

    right_critical_pixel = image.getpixel((826, 418))
    left_critical_pixel = image.getpixel((710, 418))

    person_head = image.getpixel((826, 427))
    if person_head == (51, 93, 101):
        if right_critical_pixel == back_color:
            pyautogui.moveTo(900, 1000)
            pyautogui.click(900, 1000)
        elif right_critical_pixel == tree_color:
            pyautogui.moveTo(900, 900)
            pyautogui.click(900, 900)

    else:
        if left_critical_pixel == back_color:
            pyautogui.moveTo(900, 900)
            pyautogui.click(900, 900)
        elif left_critical_pixel == tree_color:
            pyautogui.moveTo(900, 1000)
            pyautogui.click(900, 1000)
