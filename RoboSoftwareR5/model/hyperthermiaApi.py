from model.ModulesImportApi import *
from model.PortsConfigApi import *
from model.config import *

from model.DbContext import *
def F_HyperThermia():
    InstanseQDB = GeneralConnection.execute(
        "SELECT * FROM QDB WHERE nameofsymp='heat' AND state='1' ")
    for item in InstanseQDB:
        InstanseADB = GeneralConnection.execute(
            "SELECT * FROM ADB WHERE state='1' AND KindId='{}' ".format(item[TablesSchima['QDB']['KindId']]))

        if len([CheckExist for CheckExist in InstanseADB]) > 0:
            for x in range(1,50): 

                GPIO.output(PortsConfig["heating_pin"], Digital["on"])
                sleep(sleepConfigTimer["HyperThermia_delay"])
                    
            GPIO.output(PortsConfig["heating_pin"],Digital["off"])