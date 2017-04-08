#
#  LumberDoctor
# ========================================
# [] File Name : coordination_grabber.py
#
# [] Creation Date : 4/8/2017
#
# [] Created By : Ali Gholami (aligholami7596@gmail.com)
# ========================================
#
import wx

class MyFrame(wx.Frame):
    def __init__(self, parent, id, title):
        wx.Frame.__init__(self, parent, id, title)
        self.Bind(wx.EVT_MOVE, self.OnMove)
        self.Bind(wx.EVT_SIZE, self.OnSize)

    def OnSize(self, event):
        size = event.GetSize()
        print "size:", size.width, size.height

    def OnMove(self, event):
        pos = event.GetPosition()
        print "pos:", pos.x, pos.y



class MyApp(wx.App):
    def OnInit(self):
        frame = MyFrame(None, -1, "This is a test")
        frame.Show(True)
        self.SetTopWindow(frame)
        return True


def main():
    app = MyApp(0)
    app.MainLoop()


if __name__ == "__main__":
    main()
