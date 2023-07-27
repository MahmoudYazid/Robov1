from model.ModulesImportApi import *
from model.PortsConfigApi import *
from model.config import *
from model.DbContext import *
def F_HyperBreath():

	InstanseQDB = GeneralConnection.execute(
      "SELECT * FROM QDB WHERE nameofsymp='respiration' AND state='1' ")
	for item in InstanseQDB:

		InstanseADB = GeneralConnection.execute(
              "SELECT * FROM ADB WHERE state='1' AND KindId='{}' ".format(item[TablesSchima['QDB']['KindId']]))

		if len([CheckExist for CheckExist in InstanseADB]) > 0:
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
