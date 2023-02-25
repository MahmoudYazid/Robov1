from model.ModulesImportApi import *
from model.PortsConfigApi import *
from model.config import *


def F_pigmentationApi():
    for x in range(1, 6):
        
        GPIO.output(PortsConfig["led_dir1_pin"], Digital["on"])
        GPIO.output(PortsConfig["led_en_pin"], Digital["on"])

        sleep(sleepConfigTimer["pigmentation_MotorDelay"])
    GPIO.output(PortsConfig["led_dir1_pin"], Digital["off"])
    GPIO.output(PortsConfig["led_en_pin"], Digital["off"])
