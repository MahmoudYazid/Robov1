#reset analysis text -> convert it to normal range 
#reset current Db
from model.Variable import AnalysisText

from model.DbContext import *

 
def ResetAdb():
    for item in InstanseADB.find():
        InstanseADB.delete_many(item)

def F_Reset():
   
    ResetAdb()


