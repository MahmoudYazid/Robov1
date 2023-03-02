from model.ModulesImportApi import *
from model.PortsConfigApi import *
from model.config import *


def F_NormalBreath():
    GPIO.output(PortsConfig["act_dir1_pin"], Digital["off"])
    GPIO.output(PortsConfig["act_dir2_pin"], Digital["on"])
    GPIO.output(PortsConfig["act_en_pin"], Digital["on"])
    sleep(sleepConfigTimer["NormalBreath_MotorDelay"])
    GPIO.output(PortsConfig["act_dir1_pin"], Digital["on"])
    GPIO.output(PortsConfig["act_dir2_pin"], Digital["off"])
    GPIO.output(PortsConfig["act_en_pin"], Digital["on"])
    sleep(sleepConfigTimer["NormalBreath_MotorDelay"])
    GPIO.output(PortsConfig["act_dir1_pin"], Digital["off"])
    GPIO.output(PortsConfig["act_dir2_pin"], Digital["off"])
    GPIO.output(PortsConfig["act_en_pin"], Digital["off"])
