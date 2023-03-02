from model.DbContext import *
def GetInvertedArr(FindResults):
    return [int(FindResults['state'])*-1, int(FindResults['KindId'])]


def GetoriginArr(FindResults):
    return [int(FindResults['state']), int(FindResults['KindId'])]


def F_CalculateNewPhysiologicalSymptoms():
    for ADBItem in InstanseADB.find():
        inverted = GetInvertedArr(ADBItem)
        origin = GetoriginArr(ADBItem)
 
        if len([Item for Item in InstanseADB.find({"state": "{}".format(inverted[0]), "KindId":"{}".format(inverted[1])})]) > 0:
        
            InstanseADB.delete_many({"state": "{}".format(inverted[0]), "KindId":"{}".format(inverted[1])})
        
            InstanseADB.delete_many({"state": "{}".format(origin[0]), "KindId":"{}".format(origin[1])})
        else:
            continue
    return 0


