import RPi.GPIO as GPIO
import time

MAG = 32			#pin no. as per BOARD, GPIO18 as per BCM
GPIO.setwarnings(False) 	#disable warnings
GPIO.setmode(GPIO.BOARD)	#set pin numbering format
GPIO.setup(MAG, GPIO.OUT)	#set GPIO as output

try:
    print("CTRL+C for at stoppe")
    while True:
        GPIO.output(MAG,GPIO.LOW)
        print("Low")
        time.sleep(5)
        GPIO.output(MAG,GPIO.HIGH)
        print("High")
        time.sleep(5)
except KeyboardInterrupt:
    print('\n\nKeyboard exception received. Exiting.')
    exit()
