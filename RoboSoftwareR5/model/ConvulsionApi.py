from model.ModulesImportApi import *
from model.PortsConfigApi import *
from model.config import *

def F_SlowMoveApi():
    for item in InstanseQDB.find({"nameofsymp": "move", "state": "-1"}):
        if len([CheckExist for CheckExist in InstanseADB.find({"state": "-1", "KindId": item['KindId']})]) > 0:

            for x in range(1, 6):
                convulsion_motor.start(PwmStart["start"])

                GPIO.output(convulsion_dir1_pin, Digital["on"])

                convulsion_motor.ChangeDutyCycle(DegreesConfig["SlowMove"])
                sleep(sleepConfigTimer["SlowMove_MotorDelay"])

                GPIO.output(convulsion_dir1_pin, Digital["off"])
                convulsion_motor.ChangeDutyCycle(Digital["off"])

            

    
 
def F_FastMoveApi():
    for item in InstanseQDB.find({"nameofsymp": "move", "state": "1"}):
        if len([CheckExist for CheckExist in InstanseADB.find({"state": "1", "KindId": item['KindId']})]) > 0:
            convulsion_motor.start(PwmStart["start"])
            for x in range(1, 6):
                
                GPIO.output(convulsion_dir1_pin, Digital["on"])
                convulsion_motor.ChangeDutyCycle(DegreesConfig["FastMove"])
                sleep(sleepConfigTimer["FastMove_MotorDelay"])

                GPIO.output(convulsion_dir1_pin, Digital["off"])
                convulsion_motor.ChangeDutyCycle(Digital["off"])
            
   
