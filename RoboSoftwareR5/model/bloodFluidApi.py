
from model.PortsConfigApi import *
from model.config import *

def NasalBloodFluidApi():
    for item in InstanseQDB.find({"nameofsymp": "blood", "state": "1"}):
        if len([CheckExist for CheckExist in InstanseADB.find({"state": "1", "KindId": item['KindId'],"place":"nose"})]) > 0:
            
            for x in range(1, 6):
                GPIO.output(PortsConfig["blood_nose_pin"], Digital["on"])
                sleep(sleepConfigTimer["BloodWater_MotorDelay"])

                GPIO.output(PortsConfig["blood_nose_pin"], Digital["off"])

   

def MouthBloodFluidApi():
    for item in InstanseQDB.find({"nameofsymp": "blood", "state": "1"}):
        if len([CheckExist for CheckExist in InstanseADB.find({"state": "1", "KindId": item['KindId'], "place":"mouth"})]) > 0:
            for x in range(1, 6):
                GPIO.output(PortsConfig["blood_mouth_pin"], Digital["on"])
                sleep(sleepConfigTimer["BloodWater_MotorDelay"])

                GPIO.output(PortsConfig["blood_mouth_pin"], Digital["off"])
            
    
 
