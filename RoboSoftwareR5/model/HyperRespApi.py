from model.ModulesImportApi import *
from model.PortsConfigApi import *
from model.config import *

def F_HyperBreath():
	GPIO.output(PortsConfig["act_dir1_pin"], Digital["off"])
	GPIO.output(PortsConfig["act_dir2_pin"], Digital["on"])
	GPIO.output(PortsConfig["act_en_pin"], Digital["on"])
	sleep(sleepConfigTimer["HyperBreath_MotorDelay"])
	GPIO.output(PortsConfig["act_dir1_pin"], Digital["on"])
	GPIO.output(PortsConfig["act_dir2_pin"], Digital["off"])
	GPIO.output(PortsConfig["act_en_pin"], Digital["on"])
	sleep(sleepConfigTimer["HyperBreath_MotorDelay"])
	GPIO.output(PortsConfig["act_dir1_pin"], Digital["off"])
	GPIO.output(PortsConfig["act_dir2_pin"], Digital["off"])
	GPIO.output(PortsConfig["act_en_pin"], Digital["off"])
