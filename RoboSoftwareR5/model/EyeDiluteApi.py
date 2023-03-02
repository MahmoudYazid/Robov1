from model.ModulesImportApi import *
from model.PortsConfigApi import *
from model.config import *

def F_EyeDiluteApi():
    eye_motor.start(PwmStart["start"])
    for x in range(1, 6):
        

        eye_motor.ChangeDutyCycle(DegreesConfig["EyeDilute"])
        sleep(sleepConfigTimer["Eye_MotorDelay"])

        
        eye_motor.ChangeDutyCycle(Digital["off"])



