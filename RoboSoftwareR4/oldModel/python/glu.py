

import RPi.GPIO as GPIO 
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
glucose_pin=4
GPIO.setup(glucose_pin,GPIO.OUT)
glucose_motor=GPIO.PWM(glucose_pin,50)
glucose_motor.start(2.5)
def normal_glu():
	
	glucose_motor.ChangeDutyCycle(6)
	sleep(1)
	
	
	
	
def hyper_glu():
	
	glucose_motor.ChangeDutyCycle(12)
	sleep(1)
	
	
	
	
	
def hypo_glu():
	
	glucose_motor.ChangeDutyCycle(1.5)
	sleep(1)

	

for num in range(0,5):
	
	hypo_glu()
		
		
	

	
