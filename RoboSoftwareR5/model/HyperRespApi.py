from model.ModulesImportApi import *
from model.PortsConfigApi import *
from model.config import *

def F_HyperBreath():
	for item in InstanseQDB.find({"nameofsymp": "respiration", "state": "1"}):
		if len([CheckExist for CheckExist in InstanseADB.find({"state": "1", "KindId": item['KindId']})]) > 0:
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
