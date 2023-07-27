import pyttsx3
from model.DbContext import *

def Speak(text_):
    engine = pyttsx3.init()
    engine.setProperty('rate', 125)
    # say method on the engine that passing input text to be spoken
    engine.say(text_)


    # run and wait method, it processes the voice commands.
    engine.runAndWait()


def makeArrAstring(arr):
    ResutText=""

    for item in arr:
        if arr.index(item) >= len(arr)-1:

            ResutText = ResutText + " " + item 

        
        elif ResutText=="":

            ResutText = ResutText +" "+ item
        else: 
            ResutText = ResutText+" " + item 



    return ResutText


#-> get answer of (kind , state) => add to text => delete yes,no => speak 
def GetAnswerofKindandStateAndMakeText():
    print('we are here')
    InstanseADB = GeneralConnection.execute("SELECT * FROM ADB ")
    gettedAnswer=[]
    for item in InstanseADB:

        Checkexistnece = GeneralConnection.execute(
            "SELECT * FROM QDB WHERE state='{}' AND KindId='{}' ".format(item[TablesSchima['ADB']['state']], item[TablesSchima['ADB']['KindId']]))

    

        answer_ = [[answer[TablesSchima['QDB']['answer']], item[TablesSchima['ADB']['place']]]
                   for answer in Checkexistnece][0]
        print(answer_)
        spilittedAnswer=answer_[0].split()
        organ_ = answer_[1]
       
        if 'no' in spilittedAnswer:

           spilittedAnswer[spilittedAnswer.index("no")]=""
            

        if "yes" in spilittedAnswer:
           
            spilittedAnswer[spilittedAnswer.index("yes")] = ""

        if "doctor" in spilittedAnswer:
            spilittedAnswer[spilittedAnswer.index("doctor")] = ""
  
        
        if "((organ))" in spilittedAnswer:
           
            
            spilittedAnswer[int(spilittedAnswer.index("((organ))"))] = "{}".format(organ_)
        spilittedAnswer.append(",...")
        
        
        if makeArrAstring(spilittedAnswer) not in gettedAnswer:
            gettedAnswer.append(makeArrAstring(spilittedAnswer))
        
    if len(gettedAnswer)>0:  
        return makeArrAstring(gettedAnswer)
    if len(gettedAnswer) <= 0:
        return "...i feel Normal in every thing "

            
    



def tell_Me_the_Feeling():
    Speak(GetAnswerofKindandStateAndMakeText())
    return GetAnswerofKindandStateAndMakeText()

