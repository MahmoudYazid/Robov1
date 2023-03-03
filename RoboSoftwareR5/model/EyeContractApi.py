from model.ModulesImportApi import *
from model.PortsConfigApi import *
from model.config import *



def F_EyeContractApi():
    for item in InstanseQDB.find({"nameofsymp": "eye", "state": "1"}):
        if len([CheckExist for CheckExist in InstanseADB.find({"state": "1", "KindId": item['KindId']})]) > 0:

            eye_motor.start(PwmStart["start"])
            for x in range(1, 6):
                

                eye_motor.ChangeDutyCycle(DegreesConfig["EyeContract"])
                sleep(sleepConfigTimer["Eye_MotorDelay"])

                eye_motor.ChangeDutyCycle(Digital["off"])
