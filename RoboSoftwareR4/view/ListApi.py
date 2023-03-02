from model.DbContext import *
from model.Variable import *
from numpy import unique

def GetQuestions():
    for data in InstanseEDB.find():
        
        Qlist.append(data['effectorName'])
    

#implementFunc
## dont change the order of theses 2 function #######
GetQuestions()
QlistUniqueValue = Qlist
#####################################################

