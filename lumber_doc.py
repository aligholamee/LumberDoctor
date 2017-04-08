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
#   pos: 634 682
#   size : 285 * 132
#   This is when the chrome scale is set to 100% :)

# Critical region coordination
# This idea was better than my idea by Mohamad Khajavi :D
# Right_coord = 712 * 450
# Left_coord = 831 * 450

# This is the placement of Mr lumber jack
# Right_placement = 834 * 525
# Left_placement = 715 * 525

import cv2
import play_game
import pyautogui


has_won = False


while ~has_won:
    image = pyautogui.screenshot()
    right_temp_pixel = image.getpixel(712, 450)
    left_temp_pixel = image.getpixel(831,450)
    right_place = image.getpixel(834,525)
    left_place = image.getpixel(715,525)
    if right_place == (207,70,59):
        if right_temp_pixel == (211,247,255):
            # Right is ok! click right!
            play_game.click("right")
        elif right_temp_pixel == (211,247,255):
            # Right is a tree, click left
            play_game.click("left")

    elif left_place == (207,70,59):
        if left_temp_pixel == (211,247,255):
            # left is ok! click left!
            play_game.click("left")
        elif left_temp_pixel == (211,247,255):
            # left is a tree, click right
            play_game.click("right")



