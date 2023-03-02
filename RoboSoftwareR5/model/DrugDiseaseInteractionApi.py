# GET EFFECTOR ID-> get blockS OF id -> PUT IT IN active DB ->interact (may be good may be bad)
  #active database
from model.DbContext import *
from model.CalculateNewphysiologicalSymptomsApi import *

def F_GetEffectorIdByName(name): 
    return [item['Id'] for item in InstanseEDB.find({"effectorName": name})][0]


def F_GetSymptomsIdofEffectorId(Trgetedid_): 
    return [[item['SympId'], item['place']] for item in InstanseBDB.find({"EffectorId": Trgetedid_})]


def F_GetkindIdandState(symptomsIdArr):
    for KindAndStates in symptomsIdArr:
        KindAndStatesArrOfSymptom = [[item['state'], item['KindId'], KindAndStates[1]]
                                     for item in InstanseQDB.find({"SymptomId": KindAndStates[0]})][0]
        F_AddkindIdandStateinActiveDb(KindAndStatesArrOfSymptom)
        

    return 0


def F_AddkindIdandStateinActiveDb(blocksidArr_):
 
    InstanseADB.insert_one(
        {"state": blocksidArr_[0], "KindId": blocksidArr_[1], "place": blocksidArr_[2]})


def InterAct(name_):
    F_GetkindIdandState(F_GetSymptomsIdofEffectorId(
        F_GetEffectorIdByName(name_)))
    
    F_CalculateNewPhysiologicalSymptoms()
    return 0
