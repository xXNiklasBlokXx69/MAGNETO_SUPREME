import wx 
import wx.xrc

class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(parent=None, title="Hello World")
        panel = wx.Panel(self)
        my_sizer = wx.BoxSizer(wx.VERTICAL)
        staticText = wx.StaticText(panel, -1, style = wx.ALIGN_CENTER) 
        font = wx.Font(18, wx.ROMAN, wx.ITALIC, wx.NORMAL)
        staticText.SetFont(font)
        staticText.SetLabel("SORTER SØM!!!") 
        my_sizer.Add(staticText, 0, wx.ALL | wx.EXPAND, 5)
        self.text_ctrl = wx.TextCtrl(panel)
        self.text_ctrl2 = wx.TextCtrl(panel)
        self.text_ctrl3 = wx.TextCtrl(panel)
        my_sizer.Add(self.text_ctrl, 0, wx.ALL | wx.EXPAND, 5)
        my_sizer.Add(self.text_ctrl2, 0, wx.ALL | wx.EXPAND, 5)
        my_sizer.Add(self.text_ctrl3, 0, wx.ALL | wx.EXPAND, 5)
        my_btn = wx.Button(panel, label="Press Me")
        my_btn.Bind(wx.EVT_BUTTON, self.on_press)
        my_sizer.Add(my_btn, 0, wx.ALL | wx.CENTER, 5)
        self.my_resultText = wx.StaticText(panel,-1, style = wx.ALIGN_CENTER)
        self.my_resultText.SetFont(font)
        self.my_resultText.SetLabel("RESULTAT SKER HER!")
        my_sizer.Add(self.my_resultText)
        panel.SetSizer(my_sizer)
        self.Show()

    def on_press(self, event):
        value1 = self.text_ctrl.GetValue()
        value2 = self.text_ctrl2.GetValue()
        value3 = self.text_ctrl3.GetValue()
        if not value1 or not value2 or not value3:
            self.my_resultText.SetLabel("You didn't enter anything!")
        else:
            self.my_resultText.SetLabel(f'Tallenes sum er: "{int(value1) + int(value2) + int(value3)}"')

if __name__ == "__main__":
    app = wx.App()
    frame = MyFrame()
    app.MainLoop()