#reset analysis text -> convert it to normal range 
#reset current Db
from model.Variable import AnalysisText
from model.NormalGluApi import F_NormalGluApi

def F_ResetVariables():
   
    F_NormalGluApi()
 

def F_Reset():
    F_ResetVariables()


