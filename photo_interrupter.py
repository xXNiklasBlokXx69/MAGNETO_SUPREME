#!/usr/bin/env python
import RPi.GPIO as GPIO

Interupter = 36 #GPIO32 som BOARD, GPIO16 som BCM
counter = 0

def setup():
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(Interupter, GPIO.IN, pull_up_down=GPIO.PUD_UP) # Sætter pull up til high (3.3V)
	GPIO.add_event_detect(Interupter, GPIO.BOTH, callback=detect, bouncetime=200) #GPIO event
	# bouncetime (optional) minimum time between two callbacks in milliseconds (intermediate events will be ignored) 

def detect(c):
	global counter
	if GPIO.input(Interupter) == 1:
		counter += 1
		print(counter)
	if GPIO.input(Interupter) == 0:
		print("Blokeret")

def loop(): # skal kører loop hele tiden. Afrbydes af GPIO event
	while True:
		pass

def destroy():
	GPIO.cleanup() # Ryd op i GPIO

if __name__ == '__main__':
	setup()
	try:
		loop()
	except KeyboardInterrupt: # 'Ctrl+C' for at afslutte
		destroy()
