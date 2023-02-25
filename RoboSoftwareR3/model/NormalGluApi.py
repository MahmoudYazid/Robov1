from model.ModulesImportApi import *

from model.config import *

from model.Variable import AnalysisText
import random



    
def F_NormalGluApi():
   

    AnalysisText[1]="A1C Test" +" "+"{}".format(random.uniform(3, 5.6))+"%"
    AnalysisText[2]="Fasting Blood Sugar Test" +" "+"{}".format(random.randint(70, 99))+"mg/dL"

    AnalysisText[3]="Glucose Tolerance Test" +" "+"{}".format(random.randint(60, 140))+"mg/dL"




