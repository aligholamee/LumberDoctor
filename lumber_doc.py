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
# Right_coord =
# Left_coord =

import sys
sys.path.append('/usr/local/lib/python2.7/site-packages')
import wx
import cv2


app = wx.App()  # Need to create an App instance before doing anything
has_won = False

while ~has_won:
    screen = wx.ScreenDC()
    size = screen.GetSize()
    bmp = wx.EmptyBitmap(size[0], size[1])
    mem = wx.MemoryDC(bmp)
    mem.Blit(0, 0, size[0], size[1], screen, 0, 0)
    del mem  # Release bitmap
    bmp.SaveFile('screenshot.png', wx.BITMAP_TYPE_PNG)
