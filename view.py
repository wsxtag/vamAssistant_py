import wx                                       #导入wx包

# 按间距中的绿色按钮以运行脚本。
if __name__ == '__main__':

    app = wx.App()
    window = wx.Frame(None, title="wxPython Frame", size=(300, 200))
    panel = wx.Panel(window)
    label = wx.StaticText(panel, label="Hello World", pos=(100, 50))
    window.Show(True)
    app.MainLoop()