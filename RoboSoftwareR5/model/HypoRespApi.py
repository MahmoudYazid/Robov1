from model.ModulesImportApi import *
from model.PortsConfigApi import *
from model.config import *


def F_HypoBreathApi():
		GPIO.output(PortsConfig["act_dir1_pin"], Digital["off"])
		GPIO.output(PortsConfig["act_dir2_pin"], Digital["on"])
		GPIO.output(PortsConfig["act_en_pin"], Digital["on"])
		sleep(sleepConfigTimer["HypoBreath_MotorDelay"][0])
		GPIO.output(PortsConfig["act_dir1_pin"], Digital["off"])
		GPIO.output(PortsConfig["act_dir2_pin"], Digital["off"])
		GPIO.output(PortsConfig["act_en_pin"], Digital["off"])
		sleep(sleepConfigTimer["HypoBreath_MotorDelay"][1])
		GPIO.output(PortsConfig["act_dir1_pin"], Digital["on"])
		GPIO.output(PortsConfig["act_dir2_pin"], Digital["off"])
		GPIO.output(PortsConfig["act_en_pin"], Digital["on"])
		sleep(sleepConfigTimer["HypoBreath_MotorDelay"][2])
		GPIO.output(PortsConfig["act_dir1_pin"], Digital["off"])
		GPIO.output(PortsConfig["act_dir2_pin"], Digital["off"])
		GPIO.output(PortsConfig["act_en_pin"],Digital["off"])