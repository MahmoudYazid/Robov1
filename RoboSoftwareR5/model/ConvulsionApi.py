from model.ModulesImportApi import *
from model.PortsConfigApi import *
from model.config import *
from model.DbContext import *
def F_SlowMoveApi():
    InstanseQDB = GeneralConnection.execute(
        "SELECT * FROM QDB WHERE nameofsymp='move' AND state='-1' ")

    for item in InstanseQDB:
        InstanseADB = GeneralConnection.execute(
            "SELECT * FROM ADB WHERE state='-1' AND KindId='{}' ".format(item[TablesSchima['QDB']['KindId']]))

        if len([CheckExist for CheckExist in InstanseADB]) > 0:

            for x in range(1, 6):
                convulsion_motor.start(PwmStart["start"])

                GPIO.output(convulsion_dir1_pin, Digital["on"])

                convulsion_motor.ChangeDutyCycle(DegreesConfig["SlowMove"])
                sleep(sleepConfigTimer["SlowMove_MotorDelay"])

                GPIO.output(convulsion_dir1_pin, Digital["off"])
                convulsion_motor.ChangeDutyCycle(Digital["off"])

            

    
 
def F_FastMoveApi():
    InstanseQDB = GeneralConnection.execute(
        "SELECT * FROM QDB WHERE nameofsymp='move' AND state='1' ")


    for item in InstanseQDB:
        InstanseADB = GeneralConnection.execute(
            "SELECT * FROM ADB WHERE state='1' AND KindId='{}' ".format(item[TablesSchima['QDB']['KindId']]))

        if len([CheckExist for CheckExist in InstanseADB]) > 0:
            convulsion_motor.start(PwmStart["start"])
            for x in range(1, 6):
                
                GPIO.output(convulsion_dir1_pin, Digital["on"])
                convulsion_motor.ChangeDutyCycle(DegreesConfig["FastMove"])
                sleep(sleepConfigTimer["FastMove_MotorDelay"])

                GPIO.output(convulsion_dir1_pin, Digital["off"])
                convulsion_motor.ChangeDutyCycle(Digital["off"])
            
   
