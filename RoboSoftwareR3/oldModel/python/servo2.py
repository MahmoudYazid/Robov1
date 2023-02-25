

import RPi.GPIO as GPIO 

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(23,GPIO.OUT)
GPIO.setup(2,GPIO.OUT)
GPIO.setup(24,GPIO.OUT)
n=0
while 1:
	GPIO.output(24,0)
	GPIO.output(2,0)
	

	n=n+1
	
