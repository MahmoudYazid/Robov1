

from model.DbContext import *
from model.ModulesImportApi import *

from model.config import *
from model.Variable import *
import random
import numpy as np

def F_GluAnalysis(self):
	Signal=0

	for item in InstanseQDB.find({"nameofsymp":"glucose","state":"-1"}):
		if len([CheckExist for CheckExist in InstanseADB.find({"state": "-1", "KindId": item['KindId']})])>0:
			Signal=1
			self.AnalysisScreenList.addItem(
				"A1C Test" + " "+"{}".format(random.uniform(0, 2.5))+"%")
			self.AnalysisScreenList.addItem("Fasting Blood Sugar Test" +
                                   " "+"{}".format(np.random.randint(30, 50))+"mg/dL")
			self.AnalysisScreenList.addItem("Glucose Tolerance Test" +
                                   " "+"{}".format(np.random.randint(30, 50))+"mg/dL")
	for item in InstanseQDB.find({"nameofsymp": "glucose", "state": "1"}):
		if len([CheckExist for CheckExist in InstanseADB.find({"state": "1", "KindId": item['KindId']})])>0:
			Signal=1
			self.AnalysisScreenList.addItem(
			    "A1C Test" + " "+"{}".format(random.uniform(6.5, 10))+"%")

			self.AnalysisScreenList.addItem("Fasting Blood Sugar Test" + " " +
                                   "{}".format(np.random.randint(126, 130))+"mg/dL")

			self.AnalysisScreenList.addItem("Glucose Tolerance Test" + " " +
                                   "{}".format(np.random.randint(200, 250))+"mg/dL")
	if Signal==0:
		
		self.AnalysisScreenList.addItem(
				"A1C Test" + " "+"{}".format(random.uniform(3, 5.6))+"%")

		self.AnalysisScreenList.addItem("Fasting Blood Sugar Test" +
									" "+"{}".format(np.random.randint(70, 99))+"mg/dL")

		self.AnalysisScreenList.addItem("Glucose Tolerance Test" + " " +
									"{}".format(np.random.randint(60, 140))+"mg/dL")


def F_BloodPressureAnalysis(self):
	Signal = 0

	for item in InstanseQDB.find({"nameofsymp":"BP", "state":"-1"}):
		if len([CheckExist for CheckExist in InstanseADB.find({"state":"-1", "KindId": item['KindId']})]) > 0:
			Signal = 1
			self.AnalysisScreenList.addItem(
                            "Blood pressure Test" + " " +
                            "{}".format(np.random.randint(40,90)) + "/" +
                            "{}".format(np.random.randint(40,60)) + ".")

	
	for item in InstanseQDB.find({"nameofsymp": "BP", "state": "1"}):
		if len([CheckExist for CheckExist in InstanseADB.find({"state": "1", "KindId": item['KindId']})]) > 0:

			Signal = 1
			self.AnalysisScreenList.addItem("Blood pressure Test" + " "+"{}/{}".format(np.random.randint(140, 200), np.random.randint(90, 150))) 

			
	if Signal == 0:

		self.AnalysisScreenList.addItem(
                    "Blood pressure Test" + " "+"{}/{}".format(np.random.randint(90, 120), np.random.randint(60, 80))) 

		







def AutoCheck(self):
	self.AnalysisScreenList.clear()

	F_GluAnalysis(self=self)
	F_BloodPressureAnalysis(self=self)
	return 0
