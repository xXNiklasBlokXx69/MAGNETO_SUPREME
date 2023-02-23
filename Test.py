#importere packages
import wx 
import wx.xrc
from EmuControl import Emu
import RPi.GPIO as GPIO
import time
import threading

class MyFrame(wx.Frame):
    def __init__(self):#Opsætning af UI
        super().__init__(parent=None, title="Sorter Søm")#opsætning af UI
        panel = wx.Panel(self) #Lav panel til elementerne
        my_sizer = wx.BoxSizer(wx.VERTICAL)
        staticText = wx.StaticText(panel, -1, style = wx.ALIGN_CENTER) #Overskrift
        font = wx.Font(18, wx.ROMAN, wx.ITALIC, wx.NORMAL)
        staticText.SetFont(font)
        staticText.SetLabel("SORTER SØM!!!") 
        my_sizer.Add(staticText, 0, wx.ALL | wx.EXPAND, 5)#Tilføjer Overskrift til panelet
        mulighed = ["Empty","Small","Medium","Large", "Mega"]#liste med sømstørrelser
        self.listpick1 = wx.Choice(panel, choices = mulighed)#valginputs
        self.listpick2 = wx.Choice(panel, choices = mulighed)
        self.listpick3 = wx.Choice(panel, choices = mulighed)
        self.listpick4 = wx.Choice(panel, choices = mulighed)
        self.listpick5 = wx.Choice(panel, choices = mulighed)
        my_sizer.Add(self.listpick1, 0, wx.ALL | wx.CENTER, 5)#tilføj til panelet
        my_sizer.Add(self.listpick2, 0, wx.ALL | wx.CENTER, 5)
        my_sizer.Add(self.listpick3, 0, wx.ALL | wx.CENTER, 5)
        my_sizer.Add(self.listpick4, 0, wx.ALL | wx.CENTER, 5)
        my_sizer.Add(self.listpick5, 0, wx.ALL | wx.CENTER, 5)
        my_btn = wx.Button(panel, label="Press Me")#Lav knap
        my_btn.Bind(wx.EVT_BUTTON, self.on_press)#Tilføj function til knap
        my_sizer.Add(my_btn, 0, wx.ALL | wx.CENTER, 5)#Tilføj til UI
        self.my_resultText = wx.StaticText(panel,-1, style = wx.ALIGN_CENTER)#Resultattekst
        self.my_resultText.SetFont(font)
        self.my_resultText.SetLabel("RESULTAT SKER HER!")
        my_sizer.Add(self.my_resultText)#Tilføj resultattekst til UI
        panel.SetSizer(my_sizer)
        #Opsætning af motorer og magnet
        self.MAG = 32 
        self.INTERRUPTER = 36
        self.trin = 0
        self.omgange = 0
        self.max_trin = 0
        self.max_omgange = 0
        self.hastighed = 0
        self.running = False
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BOARD)#sætter GPIO på Raspberry Pi
        GPIO.setup(self.MAG, GPIO.OUT)#Sætter magnet som output
        GPIO.setup(self.INTERRUPTER, GPIO.IN, pull_up_down=GPIO.PUD_UP)  # Sætter pull up til high (3.3V)
        GPIO.add_event_detect(self.INTERRUPTER, GPIO.BOTH, callback=self.detect,bouncetime=200)
        Emu.start(self)#Starter motorer
        self.ids = Emu.scanUnits(self)#Scanner id'er 
        for id in self.ids:
            print(f"Motor id: {id}")#printer motor id i kommandoprompt
        #Sætter motor mode 
        Emu.wheelMode(self, 2)
        Emu.jointMode(self, 9)
        #Sætter magnetmotor til normal
        Emu.moveJoint(self, 9, 90)
        self.Show()#Vis UI

    def on_press(self, event):
        #Får ID af de valgte input
        choice1 = self.listpick1.GetSelection()
        choice2 = self.listpick2.GetSelection()
        choice3 = self.listpick3.GetSelection()
        choice4 = self.listpick4.GetSelection()
        choice5 = self.listpick5.GetSelection()
        #Får string, som er valgt
        value1 = self.listpick1.GetString(choice1)
        value2 = self.listpick2.GetString(choice2)
        value3 = self.listpick3.GetString(choice3)
        value4 = self.listpick4.GetString(choice4)
        value5 = self.listpick5.GetString(choice5)
        inputArr = [value1, value2, value3, value4, value5]#liste med ïnputstrenge
        for i in range(0, len(inputArr), 1):#Tjekker liste for at lave strenge om til tal
            if inputArr[i] == "Empty":
                inputArr[i] = 0
            if inputArr[i] == "Small":
                inputArr[i] = 1
            if inputArr[i] == "Medium":
                inputArr[i] = 2
            if inputArr[i] == "Large":
                inputArr[i] = 3
            if inputArr[i] == "Mega":
                inputArr[i] = 4
        self.sort_array(self, inputArr)#Funktionskald til sort_array funktion

    def OmBytSøm(self, event, tom, skruehul):
        KøreTid = skruehul * 2#tid fra start til skruen
        Tom = tom * 2 #tid fra start til tom hul
        hastighed = 200 
        SkrueTilTom = Tom - KøreTid #tid mellem hul og skrue
        #Køre hen til skrue
        Emu.moveWheel(self, 2, hastighed)    
        time.sleep(KøreTid)
        Emu.moveWheel(self, 2, 0)
        #hentsøm funktion
        self.getScrew(self)
        #hvis skrue lægger efter tom hul, så kør baglæns
        if skruehul > tom:
            hastighed *= -1
            SkrueTilTom = -SkrueTilTom
        #kør til tomt hul
        Emu.moveWheel(self, 2, hastighed)    
        time.sleep(SkrueTilTom)
        #slip skrue
        Emu.moveWheel(self, 2, 0)
        self.releaseScrew(self)
        #Hvis hastigheden ikke er baglæns, sæt den baglæns
        if hastighed >= 0:
            hastighed *= -1
        #nulstiller til start hul
        Emu.moveWheel(self, 2, hastighed)    
        time.sleep(abs(KøreTid - SkrueTilTom)+.1)
        Emu.moveWheel(self, 2, 0)
        time.sleep(1)
        return

    def sort_array(self, event, arr):
        result =  [0,1,2,3,4]
        
        while not arr == result: #indtil resultatet er det givede array
            for i in range(0, len(arr), 1):             # gennemgår tal i input array
                flag = False
                if arr[i] != i and arr[i] != 0:                # hvis array nummer ikke passer til index
                    for j in range(0, len(arr), 1):     # Gennemgår alle indexer for at finde index der indolder 0
                        if arr[j] == 0 and flag == False:      # hvis værdi i indexet er = 0 og ikke er løst før
                            
                            function1_thread = threading.Thread(target=self.OmBytSøm(self, j, i))
                            function1_thread.start()
                            function1_thread.join()
                            
                            arr[j], arr[i] = arr[i], arr[j]    # byt om på inde i og index j, opdatere vores array
                            print(arr, "  Skrue Rykket")
                            flag = True                        # flagger at vores næste ryk er bergnet
        return self.my_resultText.SetLabel("Sømmene er sorteret!")

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
    
    def getScrew(self, event):
        Emu.moveJoint(self, 9, -90)#Kør magnet ned
        GPIO.output(self.MAG, GPIO.HIGH)#tænd magnet, få skrue
        time.sleep(0.25)
        Emu.moveJoint(self, 9, 90)#Kør magnet op
    
    def releaseScrew(self, event):
        Emu.moveJoint(self, 9, 0)#Kør magnet halvvejs ned
        GPIO.output(self.MAG, GPIO.LOW)#sluk magnet, slip skrue
        time.sleep(0.25)
        Emu.moveJoint(self, 9, 90)#Kør magnet op


if __name__ == "__main__":
    app = wx.App()
    frame = MyFrame()
    app.MainLoop()