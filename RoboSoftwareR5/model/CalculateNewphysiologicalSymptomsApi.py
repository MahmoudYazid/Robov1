from model.DbContext import *
from model.config import *

def F_CalculateNewPhysiologicalSymptoms():
    for itr in range(0,20):
        InstanseADB = GeneralConnection.execute("SELECT * FROM ADB ")

        for ADBItem in InstanseADB:
            inverted = [int(ADBItem[TablesSchima['ADB']['state']])*-1,
                        int(ADBItem[TablesSchima['ADB']['KindId']])]
            origin = [int(ADBItem[TablesSchima['ADB']['state']]),int(ADBItem[TablesSchima['ADB']['KindId']])]
          
            Checkexistnece = GeneralConnection.execute("SELECT * FROM ADB WHERE state='{}' AND KindId='{}' ".format(inverted[0], inverted[1]))

            if len([Item for Item in Checkexistnece]) > 0:
            
                GeneralConnection.execute("DELETE FROM ADB WHERE state='{}' AND KindId='{}' ".format(origin[0], origin[1]))
                GeneralConnection.commit()
                GeneralConnection.execute("DELETE FROM ADB WHERE state='{}' AND KindId='{}' ".format(inverted[0], inverted[1]))
                GeneralConnection.commit()
            else:
                continue
    return 0


