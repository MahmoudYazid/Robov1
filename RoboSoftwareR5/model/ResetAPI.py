#reset analysis text -> convert it to normal range 
#reset current Db
from model.Variable import AnalysisText

from model.DbContext import *

 
def ResetAdb():
    GeneralConnection.cursor().execute("DELETE FROM ADB ")

    GeneralConnection.commit()

def F_Reset():
   
    ResetAdb()


