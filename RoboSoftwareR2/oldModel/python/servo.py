

import RPi.GPIO as GPIO 
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(23,GPIO.OUT)
GPIO.setup(2,GPIO.OUT)
GPIO.setup(24,GPIO.OUT)
def normal_breath():
	for num in range(0,5):
		
		GPIO.output(23,0)
		GPIO.output(24,1)
		GPIO.output(2,1)
		sleep(1)
		GPIO.output(23,1)
		GPIO.output(24,0)
		GPIO.output(2,1)
		sleep(1)
		GPIO.output(23,0)
		GPIO.output(24,0)
		GPIO.output(2,0)
	
def hyper_breath():
	for num in range(0,5):
		
		GPIO.output(23,0)
		GPIO.output(24,1)
		GPIO.output(2,1)
		sleep(.5)
		GPIO.output(23,1)
		GPIO.output(24,0)
		GPIO.output(2,1)
		sleep(.5)
		GPIO.output(23,0)
		GPIO.output(24,0)
		GPIO.output(2,0)
	
	
	
def hypo_breath():
	for num in range(0,5):
		
		GPIO.output(23,0)
		GPIO.output(24,1)
		GPIO.output(2,1)
		sleep(1)
		GPIO.output(23,0)
		GPIO.output(24,0)
		GPIO.output(2,0)
		sleep(2)
		GPIO.output(23,1)
		GPIO.output(24,0)
		GPIO.output(2,1)
		sleep(1)
		GPIO.output(23,0)
		GPIO.output(24,0)
		GPIO.output(2,0)
	


normal_breath()
hyper_breath()
hypo_breath()		
		
	

	
