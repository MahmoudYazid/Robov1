from model.ModulesImportApi import *
def Speak(text_):
    engine = pyttsx3.init()
    engine.setProperty('rate', 125)
    # say method on the engine that passing input text to be spoken
    engine.say(text_)


    # run and wait method, it processes the voice commands.
    engine.runAndWait()
