from EmuControl2 import Emu
import time

emu = Emu()
emu.start()
ids = emu.scanUnits()
for id in ids:
    print(str(id))

omgange = 0

# Til top-position
emu.jointMode(2)
emu.moveJoint(2, 0)

# Koerer 10 omgange og printer positionen ud.
# Positionen er fra 150 til -150
# range, speed og sleep er de tre parametre, der stilles på
emu.wheelMode(2)
for m in range(180):
  emu.moveWheel(2, 410)
  time.sleep(0.09)
  pos = emu.getPos(2)
  if pos == 150:
      omgange += 1
  print(pos)
emu.moveWheel(2,0)

print("Omgange: "+str(omgange/2))