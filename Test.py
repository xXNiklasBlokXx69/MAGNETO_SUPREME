import wx 
import wx.xrc
from EmuControl import Emu
import RPi.GPIO as GPIO

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
        mulighed = ["Empty","Small","Medium","Large"]
        self.listpick1 = wx.Choice(panel, choices = mulighed)
        self.listpick2 = wx.Choice(panel, choices = mulighed)
        self.listpick3 = wx.Choice(panel, choices = mulighed)
        self.listpick4 = wx.Choice(panel, choices = mulighed)
        my_sizer.Add(self.listpick1, 0, wx.ALL | wx.CENTER, 5)
        my_sizer.Add(self.listpick2, 0, wx.ALL | wx.CENTER, 5)
        my_sizer.Add(self.listpick3, 0, wx.ALL | wx.CENTER, 5)
        my_sizer.Add(self.listpick4, 0, wx.ALL | wx.CENTER, 5)
        my_btn = wx.Button(panel, label="Press Me")
        my_btn.Bind(wx.EVT_BUTTON, self.on_press)
        my_sizer.Add(my_btn, 0, wx.ALL | wx.CENTER, 5)
        self.my_resultText = wx.StaticText(panel,-1, style = wx.ALIGN_CENTER)
        self.my_resultText.SetFont(font)
        self.my_resultText.SetLabel("RESULTAT SKER HER!")
        my_sizer.Add(self.my_resultText)
        panel.SetSizer(my_sizer)
        #SÆT MOTOR OG MAGNET OP!
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.MAG, GPIO.OUT)
        GPIO.setup(self.INTERRUPTER, GPIO.IN, pull_up_down=GPIO.PUD_UP)  # Sætter pull up til high (3.3V)
        GPIO.add_event_detect(self.INTERRUPTER, GPIO.BOTH, callback=self.detect,bouncetime=200)
        Emu.start(self)
        self.ids = Emu.scanUnits(self)
        for id in self.ids:
            print(f"Motor id: {id}")
        self.Show()

    def on_press(self, event):
        choice1 = self.listpick1.GetSelection()
        choice2 = self.listpick2.GetSelection()
        choice3 = self.listpick3.GetSelection()
        choice4 = self.listpick4.GetSelection()
        value1 = self.listpick1.GetString(choice1)
        value2 = self.listpick2.GetString(choice2)
        value3 = self.listpick3.GetString(choice3)
        value4 = self.listpick4.GetString(choice4)
        self.my_resultText.SetLabel(f'Sømmenes Rækkefølge er: {value1},{value2},{value3},{value4}')


if __name__ == "__main__":
    app = wx.App()
    frame = MyFrame()
    app.MainLoop()