from model.ModulesImportApi import *
from model.PortsConfigApi import *
from model.config import *


def F_HyperThermia():
    for item in InstanseQDB.find({"nameofsymp": "heat", "state": "1"}):
        if len([CheckExist for CheckExist in InstanseADB.find({"state": "1", "KindId": item['KindId']})]) > 0:
            for x in range(1,50): 

                GPIO.output(PortsConfig["heating_pin"], Digital["on"])
                sleep(sleepConfigTimer["HyperThermia_delay"])
                    
            GPIO.output(PortsConfig["heating_pin"],Digital["off"])