from model.ModulesImportApi import *
from model.PortsConfigApi import *
from model.config import *



def F_HypoGluApi():
    glucose_motor.start(PwmStart["start"])
    for num in range(0, 5):

        glucose_motor.ChangeDutyCycle(DegreesConfig["HypoGlu"])
        time.sleep(sleepConfigTimer["Glu_MotorDelay"])
