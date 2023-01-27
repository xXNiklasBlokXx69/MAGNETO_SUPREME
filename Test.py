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
        self.MAG = 32 
        self.INTERRUPTER = 36
        self.trin = 0
        self.omgange = 0
        self.max_trin = 0
        self.max_omgange = 0
        self.hastighed = 0
        self.running = False
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.MAG, GPIO.OUT)
        GPIO.setup(self.INTERRUPTER, GPIO.IN, pull_up_down=GPIO.PUD_UP)  # Sætter pull up til high (3.3V)
        GPIO.add_event_detect(self.INTERRUPTER, GPIO.BOTH, callback=self.detect,bouncetime=200)
        Emu.start(self)
        self.ids = Emu.scanUnits(self)
        for id in self.ids:
            print(f"Motor id: {id}")
        Emu.wheelMode(self, 2)
        Emu.jointMode(self, 9)
        Emu.moveJoint(self, 9, 90)
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
        inputArr = [value1, value2, value3, value4]
        self.seeOrder(self, inputArr)

    def seeOrder(self, event, orderArr):
        if orderArr == ["Empty", "Small", "Medium", "Large"]:
            return self.my_resultText.SetLabel("Sømmene er sorteret!")
        elif orderArr == ["Empty", "Small", "Large", "Medium"]:
            return self.my_resultText.SetLabel(orderArr)
        elif orderArr == ["Empty", "Medium", "Small", "Large"]:
            return self.my_resultText.SetLabel(orderArr)
        elif orderArr == ["Empty", "Medium", "Large", "Small"]:
            return self.my_resultText.SetLabel(orderArr)
        elif orderArr == ["Empty", "Large", "Medium", "Small"]:
            return self.my_resultText.SetLabel(orderArr)
        elif orderArr == ["Empty", "Large", "Small", "Medium"]:
            return self.my_resultText.SetLabel(orderArr)
        elif orderArr == ["Small", "Empty", "Medium", "Large"]:
            return self.my_resultText.SetLabel(orderArr)
        elif orderArr == ["Small", "Empty", "Large", "Medium"]:
            return self.my_resultText.SetLabel(orderArr)
        elif orderArr == ["Small", "Medium", "Empty", "Large"]:
            return self.my_resultText.SetLabel(orderArr)
        elif orderArr == ["Small", "Medium", "Large", "Empty"]:
            return self.my_resultText.SetLabel(orderArr)
        elif orderArr == ["Small", "Large", "Empty", "Medium"]:
            return self.my_resultText.SetLabel(orderArr)
        elif orderArr == ["Small", "Large", "Medium", "Empty"]:
            return self.my_resultText.SetLabel(orderArr)
        elif orderArr == ["Medium", "Empty", "Small", "Large"]:
            return self.my_resultText.SetLabel(orderArr)
        elif orderArr == ["Medium", "Empty", "Large", "Small"]:
            return self.my_resultText.SetLabel(orderArr)
        elif orderArr == ["Medium", "Small", "Empty", "Large"]:
            return self.my_resultText.SetLabel(orderArr)
        elif orderArr == ["Medium", "Small", "Large", "Empty"]:
            return self.my_resultText.SetLabel(orderArr)
        elif orderArr == ["Medium", "Large", "Empty", "Small"]:
            return self.my_resultText.SetLabel(orderArr)
        elif orderArr == ["Medium", "Large", "Small", "Empty"]:
            return self.my_resultText.SetLabel(orderArr)
        elif orderArr == ["Large", "Empty", "Small", "Medium"]:
            return self.my_resultText.SetLabel(orderArr)
        elif orderArr == ["Large", "Empty", "Medium", "Small"]:
            return self.my_resultText.SetLabel(orderArr)
        elif orderArr == ["Large", "Small", "Empty", "Medium"]:
            return self.my_resultText.SetLabel(orderArr)
        elif orderArr == ["Large", "Small", "Medium", "Empty"]:
            return self.my_resultText.SetLabel(orderArr)
        elif orderArr == ["Large", "Medium", "Empty", "Small"]:
            return self.my_resultText.SetLabel(orderArr)
        elif orderArr == ["Large", "Medium", "Small", "Empty"]:
            return self.my_resultText.SetLabel(orderArr)
        else:
            return self.my_resultText.SetLabel("Du har indtastet noget forkert!")
        


    def detect(self,c):
        if self.running:
            if GPIO.input(self.INTERRUPTER) == 1:
                self.trin += 1
                #print(self.trin)
                if self.trin >= 4: # 4 = antallet af huller i skiven foran motoren
                    self.omgange += 1
                    self.trin = 0
                if self.omgange >= self.max_omgange and self.trin >= self.max_trin:
                    print("Omgang: "+str(self.omgange))
                    print("Trin: "+str(self.trin))
                    Emu.moveWheel(self, int(self.valgtMotor), 0)
                    self.running = False


if __name__ == "__main__":
    app = wx.App()
    frame = MyFrame()
    app.MainLoop()