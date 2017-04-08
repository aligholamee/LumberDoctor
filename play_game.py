import pyautogui

def click(dir):

    if dir == 1:
        pyautogui.moveTo(852,706)
        pyautogui.click(852, 706)

    elif dir == 0:
        pyautogui.moveTo(684, 706)
        pyautogui.click(684, 706)