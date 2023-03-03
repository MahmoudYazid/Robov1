from model.ModulesImportApi import *
from model.PortsConfigApi import *
from model.config import *

def F_NasalWaterFluidApi():
    for item in InstanseQDB.find({"nameofsymp": "water", "state": "1"}):
        if len([CheckExist for CheckExist in InstanseADB.find({"state": "1", "KindId": item['KindId'], "place":"nose"})]) > 0:
            for x in range(1, 6):
                GPIO.output(PortsConfig["water_nose_pin"], 1)
                sleep(sleepConfigTimer["BloodWater_MotorDelay"])
            GPIO.output(PortsConfig["water_nose_pin"], 0)

    return 0


def F_MouthWaterFluidApi():
    for item in InstanseQDB.find({"nameofsymp": "water", "state": "1"}):
        if len([CheckExist for CheckExist in InstanseADB.find({"state": "1", "KindId": item['KindId'], "place":"mouth"})]) > 0:
            for x in range(1,6):
                GPIO.output(PortsConfig["water_mouth_pin"], 1)
                sleep(sleepConfigTimer["BloodWater_MotorDelay"])
                
            GPIO.output(PortsConfig["water_mouth_pin"], 0)
            
