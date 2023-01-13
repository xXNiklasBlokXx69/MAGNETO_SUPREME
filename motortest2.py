from EmuControl2 import Emu
import time

emu = Emu()
emu.start()
ids = emu.scanUnits()
for id in ids:
    print(str(id))

emu.jointMode(2)
emu.moveJoint(2, 0)

def omgange(omg):
    for i in range(0,omg):
        emu.moveJoint(2,150)
        emu.wheelMode(2)
        emu.moveWheel(2, 600)
        time.sleep(0.1)
        emu.jointMode(2)
        emu.moveJoint(2, -150)
    emu.moveJoint(2, 0)

omgange(2)
