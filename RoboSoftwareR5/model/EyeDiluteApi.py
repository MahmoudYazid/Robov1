from model.ModulesImportApi import *
from model.PortsConfigApi import *
from model.config import *
from model.DbContext import *
def F_EyeDiluteApi():
    InstanseQDB = GeneralConnection.execute(
        "SELECT * FROM QDB WHERE nameofsymp='eye' AND state='-1' ")

    for item in InstanseQDB:
        InstanseADB = GeneralConnection.execute(
            "SELECT * FROM ADB WHERE state='-1' AND KindId='{}' ".format(item[TablesSchima['QDB']['KindId']]))

        if len([CheckExist for CheckExist in InstanseADB]) > 0:
            eye_motor.start(PwmStart["start"])
            for x in range(1, 6):
                

                eye_motor.ChangeDutyCycle(DegreesConfig["EyeDilute"])
                sleep(sleepConfigTimer["Eye_MotorDelay"])

                
                eye_motor.ChangeDutyCycle(Digital["off"])



