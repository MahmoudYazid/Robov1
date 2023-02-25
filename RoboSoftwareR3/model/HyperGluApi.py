from model.config import *
from model.Variable import AnalysisText
import random



def F_HyperGluApi():
    
    AnalysisText[1]="A1C Test" +" "+"{}".format(random.uniform(6.5, 10))+"%"

    AnalysisText[2] = "Fasting Blood Sugar Test" + " "+"{}".format(random.randint(126, 130))+"mg/dL"

    AnalysisText[3]="Glucose Tolerance Test" +" "+"{}".format(random.randint(200, 250))+"mg/dL"
    



	    



