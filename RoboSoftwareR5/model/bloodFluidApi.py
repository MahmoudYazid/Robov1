
from model.PortsConfigApi import *
from model.config import *
from model.DbContext import *
def NasalBloodFluidApi():
    InstanseQDB = GeneralConnection.execute(
        "SELECT * FROM QDB WHERE nameofsymp='blood' AND state='1' ")
    for item in InstanseQDB:
        InstanseADB = GeneralConnection.execute(
            "SELECT * FROM ADB WHERE state='1' AND KindId='{}' AND place='nose' ".format(item[TablesSchima['QDB']['KindId']]))
        if len([CheckExist for CheckExist in InstanseADB]) > 0:
            
            for x in range(1, 6):
                GPIO.output(PortsConfig["blood_nose_pin"], Digital["on"])
                sleep(sleepConfigTimer["BloodWater_MotorDelay"])

                GPIO.output(PortsConfig["blood_nose_pin"], Digital["off"])

   

def MouthBloodFluidApi():
    InstanseQDB = GeneralConnection.execute(
        "SELECT * FROM QDB WHERE nameofsymp='blood' AND state='1' ")

    for item in InstanseQDB:
        InstanseADB = GeneralConnection.execute(
            "SELECT * FROM ADB WHERE state='1' AND KindId='{}' AND place='mouth' ".format(item[TablesSchima['QDB']['KindId']]))

        if len([CheckExist for CheckExist in InstanseADB]) > 0:
            for x in range(1, 6):
                GPIO.output(PortsConfig["blood_mouth_pin"], Digital["on"])
                sleep(sleepConfigTimer["BloodWater_MotorDelay"])

                GPIO.output(PortsConfig["blood_mouth_pin"], Digital["off"])
            
    
 
