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



import cv2
import play_game
import pyautogui


has_won = False

while ~has_won:
    image = pyautogui.screenshot()
    right_temp_pixel = image.getpixel(712, 450)
    left_temp_pixel = image.getpixel(831,450)



