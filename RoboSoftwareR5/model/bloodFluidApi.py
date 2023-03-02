
from model.PortsConfigApi import *
from model.config import *

def NasalBloodFluidApi():
    for x in range(1, 6):
        GPIO.output(PortsConfig["blood_nose_pin"], Digital["on"])
        sleep(sleepConfigTimer["BloodWater_MotorDelay"])

        GPIO.output(PortsConfig["blood_nose_pin"], Digital["off"])

   

def MouthBloodFluidApi():
    for x in range(1, 6):
        GPIO.output(PortsConfig["blood_mouth_pin"], Digital["on"])
        sleep(sleepConfigTimer["BloodWater_MotorDelay"])

        GPIO.output(PortsConfig["blood_mouth_pin"], Digital["off"])
    
    
 
