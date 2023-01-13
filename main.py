#coding: utf8
import wx
import gui
from EmuControl import Emu
import RPi.GPIO as GPIO

class mainFrame(gui.MainFrame):
    def __init__(self, parent):
        gui.MainFrame.__init__(self, parent)
        self.valgtMotor = 0
        self.valgtPosition = 0
        self.MAG = 32 #GPIO32 som BOARD, GPIO16 som BCM
        self.INTERRUPTER = 36
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.MAG, GPIO.OUT)
        GPIO.setup(self.INTERRUPTER, GPIO.IN, pull_up_down=GPIO.PUD_UP)  # Sætter pull up til high (3.3V)
        GPIO.add_event_detect(self.INTERRUPTER, GPIO.BOTH, callback=self.detect,bouncetime=200)
        # bouncetime (optional) minimum time between two callbacks in milliseconds (intermediate events will be ignored) 
        self.trin = 0
        self.omgange = 0
        self.max_trin = 0
        self.max_omgange = 0
        self.hastighed = 0
        self.running = False
        Emu.start(self)
        self.ids = Emu.scanUnits(self)
        for id in self.ids:
            self.id_choice.Append(str(id))
            self.id_choice2.Append(str(id))

    def OnExit( self, event ):
        GPIO.cleanup()  # Ryd op i GPIO
        exit(0)

    def OnOn( self, event ):
        wx.MessageBox('Magneten tændt!', 'Magnet', wx.OK)
        GPIO.output(self.MAG, GPIO.HIGH)

    def OnOff( self, event ):
        wx.MessageBox('Magneten slukket!', 'Magnet', wx.OK)
        GPIO.output(self.MAG, GPIO.LOW)

    def OnValg( self, event ):
        self.valgtMotor = self.id_choice.GetStringSelection()
        #wx.MessageBox('Valgt motor: ' + self.valgtMotor, 'Motor', wx.OK)

    def OnGoto( self, event ):
        self.valgtPosition = self.spin_pos.GetValue()
        #wx.MessageBox('Motoren kører til position: ' + str(self.valgtPosition), 'Postion', wx.OK)
        Emu.jointMode(self, int(self.valgtMotor))
        Emu.moveJoint(self, int(self.valgtMotor), self.valgtPosition)

    def OnValg2( self, event ):
        self.valgtMotor = self.id_choice2.GetStringSelection()

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

    def run(self, event):
        self.running = True
        self.omgange = 0
        self.trin = 0
        self.max_trin = self.spin_trin.GetValue()
        self.max_omgange = self.spin_omgange.GetValue()
        self.hastighed = int(self.lst_hastighed.GetStringSelection())
        Emu.wheelMode(self, int(self.valgtMotor))
        if self.radio_retning.GetSelection()== 1:
            self.hastighed *= -1
        Emu.moveWheel(self,int(self.valgtMotor), self.hastighed)

    def stop(self, event):
        Emu.moveWheel(self, int(self.valgtMotor), 0 )


app = wx.App(False)
frame = mainFrame(None)
frame.Show(True)
app.MainLoop()
