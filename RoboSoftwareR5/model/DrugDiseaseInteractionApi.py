# GET EFFECTOR ID-> get blockS OF id -> PUT IT IN active DB ->interact (may be good may be bad)
  #active database
from model.DbContext import *
from model.CalculateNewphysiologicalSymptomsApi import *
from model.config import *
def F_GetEffectorIdByName(name):
    F_GetEffectorIdByNameCursur=GeneralConnection.execute(
        "SELECT * FROM EDB WHERE effectorName='{}'".format(name))
    
    return [item[TablesSchima['EDB']['Id']] for item in F_GetEffectorIdByNameCursur][0]


def F_GetSymptomsIdofEffectorId(Trgetedid_): 
   
  
    F_GetSymptomsIdofEffectorIdCursur = GeneralConnection.execute(
        "SELECT * FROM BDB WHERE EffectorId='{}'".format(Trgetedid_))

    F_GetSymptomsIdofEffectorIdaRR=[[item[TablesSchima['BDB']['SympId']], item[TablesSchima['BDB']['place']]]
          for item in F_GetSymptomsIdofEffectorIdCursur]

    return F_GetSymptomsIdofEffectorIdaRR

def F_GetkindIdandState(symptomsIdArr):

    for KindAndStates in symptomsIdArr:
        F_GetkindIdandStateCursur = GeneralConnection.execute(
            "SELECT * FROM QDB WHERE SymptomId='{}'".format(KindAndStates[0]))

        KindAndStatesArrOfSymptom = [[item[TablesSchima['QDB']['state']], item[TablesSchima['QDB']['KindId']], KindAndStates[1]]
                                     for item in F_GetkindIdandStateCursur][0]
      
        GeneralConnection.cursor().execute(
            "INSERT INTO ADB (state,KindId,place) VALUES ('{}','{}','{}')".format(KindAndStatesArrOfSymptom[0], KindAndStatesArrOfSymptom[1], KindAndStatesArrOfSymptom[2]))

        GeneralConnection.commit()
        

    return 0



def InterAct(name_):
   

    GetId=F_GetEffectorIdByName(name_)
    SympIdArr=F_GetSymptomsIdofEffectorId(GetId)

    F_GetkindIdandState(SympIdArr)
    
    F_CalculateNewPhysiologicalSymptoms()
    return 0
