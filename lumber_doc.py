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

# The button area coordination:
#
#
#   This is when the chrome scale is set to 100% :)

# Critical region coordination
# This idea was better than my idea by Mohamad Khajavi :D
# Right_coord = 712 * 450
# Left_coord = 831 * 450

# This is the placement of Mr lumber jack
# Right_placement = 834 * 525
# Left_placement = 715 * 525


import play_game
import pyautogui
import time

# Wait until the game runs
time.sleep(5)

while True:
    image = pyautogui.screenshot()
    right_critical_pixel = image.getpixel((826, 418))
    left_critical_pixel = image.getpixel((710, 418))

    right_place = image.getpixel((823, 494))
    left_place = image.getpixel((707, 494))

    tree_color = (161, 116, 56)
    back_color = (211, 247, 255)

    if right_place == (207, 70, 59):
        if right_critical_pixel == back_color:
            # Right is ok! click right!
            play_game.click(1)
            print("Right is OK!")
        elif right_critical_pixel == tree_color:
            # Right is a tree, click left
            play_game.click(0)
            print("Right is a tree!")

    elif left_place == (207, 70, 59):
        if left_critical_pixel == back_color:
            # left is ok! click left!
            play_game.click(0)
            print("Left is ok!")
        elif left_critical_pixel == tree_color:
            # left is a tree, click right
            play_game.click(1)
            print("Left is a tree!")
