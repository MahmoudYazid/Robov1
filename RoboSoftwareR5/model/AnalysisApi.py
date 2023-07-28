

from model.DbContext import *
from model.ModulesImportApi import *

from model.config import *
from model.Variable import *
import random
import numpy as np
import tkinter as tk
from tkinter import ttk
from datetime import datetime
def F_GluAnalysis(self):
	Signal=0
	InstanseQDB = GeneralConnection.execute(
		"SELECT * FROM QDB WHERE nameofsymp='glucose' AND state='-1' ")
	for item in InstanseQDB:
		InstanseADB = GeneralConnection.execute(
			"SELECT * FROM ADB WHERE state='-1' AND KindId='{}' ".format(item[TablesSchima['QDB']['KindId']]))
		if len([CheckExist for CheckExist in InstanseADB])>0:
			Signal=1
			self.AnalysisScreenList.insert(
				"A1C Test" + " "+"{}".format(random.uniform(0, 2.5))+"%")
			self.AnalysisScreenList.insert(tk.END, "Fasting Blood Sugar Test" +
                                   " "+"{}".format(np.random.randint(30, 50))+"mg/dL")
			self.AnalysisScreenList.insert(tk.END, "Glucose Tolerance Test" +
                                   " "+"{}".format(np.random.randint(30, 50))+"mg/dL")
	
	InstanseQDB2 = GeneralConnection.execute(
		"SELECT * FROM QDB WHERE nameofsymp='glucose' AND state='1' ")

	for item in InstanseQDB2:
		InstanseADB = GeneralConnection.execute(
			"SELECT * FROM ADB WHERE state='1' AND KindId='{}' ".format(item[TablesSchima['QDB']['KindId']]))
	

		if len([CheckExist for CheckExist in InstanseADB])>0:
			Signal=1
			self.AnalysisScreenList.insert(tk.END,
			    "A1C Test" + " "+"{}".format(random.uniform(6.5, 10))+"%")

			self.AnalysisScreenList.insert(tk.END,"Fasting Blood Sugar Test" + " " +
                                   "{}".format(np.random.randint(126, 130))+"mg/dL")

			self.AnalysisScreenList.insert(tk.END,"Glucose Tolerance Test" + " " +
                                   "{}".format(np.random.randint(200, 250))+"mg/dL")
	if Signal==0:
		
		self.AnalysisScreenList.insert(tk.END,
				"A1C Test" + " "+"{}".format(random.uniform(3, 5.6))+"%")

		self.AnalysisScreenList.insert(tk.END,"Fasting Blood Sugar Test" +
									" "+"{}".format(np.random.randint(70, 99))+"mg/dL")

		self.AnalysisScreenList.insert(tk.END, "Glucose Tolerance Test" + " " +
									"{}".format(np.random.randint(60, 140))+"mg/dL")


def F_BloodPressureAnalysis(self):
	Signal = 0


	InstanseQDB = GeneralConnection.execute(
            "SELECT * FROM QDB WHERE nameofsymp='BP' AND state='-1' ")

	for item in InstanseQDB:
		InstanseADB=GeneralConnection.execute(
                    "SELECT * FROM ADB WHERE state='-1' AND KindId='{}' ".format(item[TablesSchima['QDB']['KindId']]))

		if len([CheckExist for CheckExist in InstanseADB]) > 0:
			Signal = 1
			self.AnalysisScreenList.insert(tk.END,
                            "Blood pressure Test" + " " +
                            "{}".format(np.random.randint(40,90)) + "/" +
                            "{}".format(np.random.randint(40,60)) + ".")

	
	InstanseQDB2 = GeneralConnection.execute(
            "SELECT * FROM QDB WHERE nameofsymp='BP' AND state='1' ")

	for item in InstanseQDB2:
		InstanseADB = GeneralConnection.execute(
                    "SELECT * FROM ADB WHERE state='1' AND KindId='{}' ".format(item[TablesSchima['QDB']['KindId']]))

		if len([CheckExist for CheckExist in InstanseADB]) > 0:

			Signal = 1
			self.AnalysisScreenList.insert(tk.END,"Blood pressure Test" + " "+"{}/{}".format(np.random.randint(140, 200), np.random.randint(90, 150))) 

			
	if Signal == 0:

		self.AnalysisScreenList.insert(tk.END,"Blood pressure Test" + " "+"{}/{}".format(np.random.randint(90, 120), np.random.randint(60, 80))) 

		







def AutoCheck(self):
	self.AnalysisScreenList.delete(0, tk.END)

	F_GluAnalysis(self=self)
	F_BloodPressureAnalysis(self=self)
	return 0
