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

import wx

# Take an screenshot of the current page
wx.App()    # Need to create an App instance before doing anything
screen = wx.ScreenDC()
size = screen.getSize()
