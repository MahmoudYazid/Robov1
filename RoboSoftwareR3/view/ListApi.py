from model.DbContext import *
from model.Variable import *
from numpy import unique

def GetQuestions():
    for data in InstanseQdb.find():
        Qlist.append(list(data.items())[QuestionColum][QuestionText])
    

def getUniqueArr():
    Newarr=set()
    arranged = Qlist
    for item in arranged:
        Newarr.add(item)
        

    return list(Newarr)






#implementFunc
## dont change the order of theses 2 function #######
GetQuestions()
QlistUniqueValue=getUniqueArr()
#####################################################

