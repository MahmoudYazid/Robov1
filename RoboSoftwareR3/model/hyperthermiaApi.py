from model.ModulesImportApi import *
from model.PortsConfigApi import *
from model.config import *


def F_HyperThermia():
    for x in range(1,50): 

        GPIO.output(PortsConfig["heating_pin"], Digital["on"])
        sleep(sleepConfigTimer["HyperThermia_delay"])
            
    GPIO.output(PortsConfig["heating_pin"],Digital["off"])