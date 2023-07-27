from model.ModulesImportApi import *
from model.PortsConfigApi import *
from model.config import *
from model.DbContext import *
def F_NasalWaterFluidApi():
    InstanseQDB = GeneralConnection.execute(
        "SELECT * FROM QDB WHERE nameofsymp='water' AND state='1' ")

    for item in InstanseQDB:
        InstanseADB = GeneralConnection.execute(
            "SELECT * FROM ADB WHERE state='1' AND KindId='{}' AND place='nose' ".format(item[TablesSchima['QDB']['KindId']]))

        if len([CheckExist for CheckExist in InstanseADB]) > 0:
            for x in range(1, 6):
                GPIO.output(PortsConfig["water_nose_pin"], 1)
                sleep(sleepConfigTimer["BloodWater_MotorDelay"])
            GPIO.output(PortsConfig["water_nose_pin"], 0)

    return 0


def F_MouthWaterFluidApi():
    InstanseQDB = GeneralConnection.execute(
        "SELECT * FROM QDB WHERE nameofsymp='water' AND state='1' ")

    for item in InstanseQDB:
        InstanseADB = GeneralConnection.execute(
            "SELECT * FROM ADB WHERE state='1' AND KindId='{}' AND place='mouth' ".format(item[TablesSchima['QDB']['KindId']]))


        if len([CheckExist for CheckExist in InstanseADB]) > 0:
            for x in range(1,6):
                GPIO.output(PortsConfig["water_mouth_pin"], 1)
                sleep(sleepConfigTimer["BloodWater_MotorDelay"])
                
            GPIO.output(PortsConfig["water_mouth_pin"], 0)
            
