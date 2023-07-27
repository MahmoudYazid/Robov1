from model.DbContext import *
from model.Variable import *
from model.config import *

def GetQuestions():
    
    GetQuestions = GeneralConnection.cursor().execute("SELECT * FROM EDB ")
    for data in GetQuestions:
        
        Qlist.append(data[TablesSchima['EDB']['effectorName']])
    

#implementFunc
## dont change the order of theses 2 function #######
GetQuestions()
QlistUniqueValue = Qlist
#####################################################

