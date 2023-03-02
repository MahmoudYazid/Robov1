
import sqlite3 as sql

import pyttsx3
import datetime


import easygui

from time import sleep

import matplotlib.pyplot as plt

from matplotlib.animation import FuncAnimation

import RPi.GPIO as GPIO 
from pylinks import *




def unique(list1):
    unique_list = []

# traverse for all elements
    for x in list1:
        # check if exists in unique_list or not
        if x not in unique_list:
            unique_list.append(x)
    # print list
    return unique_list

result_of_talk_array=[]
final_results = []
sumition = 0
result=""
get_feeling_tube=[]
speed=150
fig = plt.figure(figsize=(6, 3))

def update_hyper_bp(frame):
    
    global last_x
    global last_y
    global cycle_no
    x.append(last_x)
    last_x=last_x+1

    #y
    y.append(y_hypo[last_y])
    last_y=last_y+1
    cycle_no=cycle_no+1
    if y_hypo[last_y-1]==-2 and cycle_no==len(y_hypo):
        cycle_no=0
        last_y=0
    ln.set_data(x, y)
    if (last_x == 100):
        plt.close(fig)

    return ln,

def jeckvoice(text):


    # Import the required module for text
	# to speech conversion

	# init function to get an engine instance for the speech synthesis
    engine = pyttsx3.init()
    engine.setProperty("rate", speed)
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[3].id)

    # say method on the engine that passing input text to be spoken
    engine.say("{}".format(text))

    # run and wait method, it processes the voice commands.
    engine.runAndWait()
    return 0

# Function to convert text to


choices_array_final = ["talk slower please","talk faster please","show me the symptoms that you feel"]
glucose_pin=4
eye_pin=17
blood_nose_pin=27
blood_mouth_pin=18
water_nose_pin=22
water_mouth_pin=25

act_en_pin=2
act_dir1_pin=23
act_dir2_pin=24

convulsion_en_pin=16
convulsion_dir1_pin=20

led_en_pin=5
led_dir1_pin=6

heating_pin=26

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(glucose_pin,GPIO.OUT)
GPIO.setup(eye_pin,GPIO.OUT)
GPIO.setup(blood_mouth_pin,GPIO.OUT)
GPIO.setup(blood_nose_pin,GPIO.OUT)
GPIO.setup(water_mouth_pin,GPIO.OUT)
GPIO.setup(water_nose_pin,GPIO.OUT) 
GPIO.setup(act_dir1_pin,GPIO.OUT)
GPIO.setup(act_dir2_pin,GPIO.OUT)
GPIO.setup(act_en_pin,GPIO.OUT)
GPIO.setup(convulsion_dir1_pin,GPIO.OUT)
GPIO.setup(convulsion_en_pin,GPIO.OUT)
GPIO.setup(led_dir1_pin,GPIO.OUT) 
GPIO.setup(led_en_pin,GPIO.OUT) 
GPIO.setup(heating_pin,GPIO.OUT) 


GPIO.setup(23,GPIO.OUT)
GPIO.setup(2,GPIO.OUT)
GPIO.setup(24,GPIO.OUT)

convulsion_motor=GPIO.PWM(convulsion_en_pin,50) 
eye_motor=GPIO.PWM(eye_pin,50) 
glucose_motor=GPIO.PWM(glucose_pin,50)


	
def hypo_breath():
		GPIO.output(23,0)
		GPIO.output(24,1)
		GPIO.output(2,1)
		sleep(1)
		GPIO.output(23,0)
		GPIO.output(24,0)
		GPIO.output(2,0)
		sleep(2)
		GPIO.output(23,1)
		GPIO.output(24,0)
		GPIO.output(2,1)
		sleep(1)
		GPIO.output(23,0)
		GPIO.output(24,0)
		GPIO.output(2,0)

def hyper_breath():		
		GPIO.output(23,0)
		GPIO.output(24,1)
		GPIO.output(2,1)
		sleep(.5)
		GPIO.output(23,1)
		GPIO.output(24,0)
		GPIO.output(2,1)
		sleep(.5)
		GPIO.output(23,0)
		GPIO.output(24,0)
		GPIO.output(2,0)

def normal_breath():
    GPIO.output(23,0)
    GPIO.output(24,1)
    GPIO.output(2,1)
    sleep(1)
    GPIO.output(23,1)
    GPIO.output(24,0)
    GPIO.output(2,1)
    sleep(1)
    GPIO.output(23,0)
    GPIO.output(24,0)
    GPIO.output(2,0)

def normal_glu():
	
	glucose_motor.ChangeDutyCycle(6)
	sleep(1)
	
	
	
	
def hyper_glu():
	
	glucose_motor.ChangeDutyCycle(12)
	sleep(1)
	
	
	
	
	
def hypo_glu():
	
	glucose_motor.ChangeDutyCycle(1.5)
	sleep(1)
    
last_x=0
last_y=0
cycle_no=0
y_hypo=[0,0,1,1,-1,.5,.5,-5,7,8,9,-.5,-2]


if __name__=="__main__":

    while 1 :
        

       
                #if order of disease
    #------------------------------------------------------------------
        con = sql.connect("{}".format(sql_db_link))
        cur = con.cursor()
        
        get_choices = cur.execute("SELECT question FROM quistions_db")
        for get_choices_result in get_choices:
            
            choices_array_final.append(get_choices_result[0])

        get_choices2 = cur.execute("SELECT effector,type_effector FROM blocks")
        for get_choices_result2 in get_choices2.fetchall():
            if "{}".format(get_choices_result2[1]) == "drug":
                text = "take {} {}".format("{}".format(
                    get_choices_result2[1]), "{}".format(get_choices_result2[0]))
                choices_array_final.append(text)
            if "{}".format(get_choices_result2[1]) == "disease":
                text = "make {} {}".format("{}".format(
                    get_choices_result2[1]), "{}".format(get_choices_result2[0]))
                choices_array_final.append(text)
       
        #what he real feel
       
        get_feel = cur.execute(
            "SELECT nameofsymp FROM quistions_db WHERE activate_state='a' ")
        for get_feel_result in get_feel.fetchall():
            get_feeling_tube.append(get_feel_result[0])
       
            
            
        if len(get_feeling_tube)==0:
            
            result = easygui.choicebox(choices=unique(choices_array_final),msg="what i feel : {}".format("no clinical issues i think"))
            
        if len(get_feeling_tube) > 0:
            
            result = easygui.choicebox(choices=unique(
                choices_array_final), msg="what i feel : {}".format([i for i in get_feeling_tube]))
        
        if result=="talk slower please":
            speed=speed-50
        if result == "talk faster please":
            speed = speed + 50

        result_of_talk_array.clear()
        get_feeling_tube.clear()
        result_of_talk_array.append("{}".format(result))
        #status asking 
        get_status = cur.execute(
            "SELECT answer FROM quistions_db WHERE nameofsymp='status' and question='{}'  ".format(result))
        for status_result in get_status.fetchall():
            if len(status_result)!= 0 :  
                jeckvoice("{}".format(status_result[0]))
       
       
#--------------------------------------------------------------------------------
       
        #show symptoms
        if "show me the symptoms that you feel" in result_of_talk_array[0]:
            


            physics_symp_arr=[]
            import sqlite3 as sql
            con_res = sql.connect("{}".format(sql_db_link))
            cur_res = con_res.cursor()
        
            c1=cur_res.execute("SELECT nameofsymp,state,place FROM quistions_db  WHERE activate_state='a'")
            rows=c1.fetchall()
            
            for r in rows:
                physics_symp_arr.append(r)
            
            if len(physics_symp_arr) != 0 :
                
                n=0
                
                
                
             
                
                
                
                while n<1 :
                   
                    for ex in physics_symp_arr:
                        
                        if "respiration" == "{}".format(ex[0]):
                            
                            for x in range(1,6):

                                
                            
                                if "{}".format(ex[1]) == "-1":
                                        
                                        
                                    
                                        hypo_breath()
                                        sleep(1)
                                       
                                

                                    
                        
                                if "{}".format(ex[1]) == "1":
                              
                                    hyper_breath()
                                    sleep(1)
                                    
                                    
                                    
                                    
                                
                                    
                                    
                        #------------------------------------
                        if "pigmentation" == "{}".format(ex[0]):
                            
                            for x in range(1,6):

                                
                            
                                

                                if "{}".format(ex[1]) == "1":
                                    GPIO.output(PortsConfig["led_dir1_pin"], 1)
                                    GPIO.output(PortsConfig["led_en_pin"], 1)


                                    sleep(0.5)
                                
                                    
                                GPIO.output(PortsConfig["led_dir1_pin"],0)
                                GPIO.output(PortsConfig["led_en_pin"], 0)


                            #---------------------------
                                    
                        if "eye" == "{}".format(ex[0]):
                            #eye_motor
                            
                            for x in range(1,6):
                                eye_motor.start(2.5)
                                
                            
                                if "{}".format(ex[1]) == "-1":
                                        
                                        
                                    
                                        eye_motor.ChangeDutyCycle(12)
                                        sleep(0.5)


                                       
                                

                                    
                        
                                if "{}".format(ex[1]) == "1":
                              
                                    


                                    
                                    
                                    eye_motor.ChangeDutyCycle(1)
                                    sleep(.5)

                                
                            
                                eye_motor.ChangeDutyCycle(0)
                        
                        
                        
                        #-------------------------------
                        if "glucose" == "{}".format(ex[0]):
                            
                            #glucose_motor
                           
                        
                            for x in range(1,6):
                                glucose_motor.start(2.5)
                                
                            
                                if "{}".format(ex[1]) == "-1":
                                    hypo_glu()
                                        
                                        
                                    
                                        


                                       
                                

                                    
                        
                                if "{}".format(ex[1]) == "1":
                                    hyper_glu()
                                    
                                    
                                
                                
                    
                        
                        
                            
                        
                       #-----------------------                 
                        if "BP" == "{}".format(ex[0]):
                            
                            
                            #bp_motor
                           
                        
                            
                            
                        
                            if "{}".format(ex[1]) == "-1":
                                
                                
                                x = [0]
                                y = [0]

                                ln,= plt.plot(x, y, '-')
                                plt.axis([0, 100, 0, 100])

                                animation = FuncAnimation(fig, update_hyper_bp, interval=150)
                                plt.show()
                                                                        
                                                                        
                                


                                   
                            

                                
                    
                            if "{}".format(ex[1]) == "1":
                          
                                


                                
                                x = [0]
                                y = [0]

                                ln,= plt.plot(x, y, '-')
                                plt.axis([0, 100, 0, 10])

                                animation = FuncAnimation(fig, update_hyper_bp, interval=150)
                                plt.show()
                                
                         #-----------------------                 
                        
                        if "water" == "{}".format(ex[0]) and "nose" == "{}".format(ex[2]) :
                            
                            
                            #nasal_fluid_motor
                           
                            
                            for x in range(1,6):
                                
                                
                            
            
                        
                                if "{}".format(ex[1]) == "1":
                              
                                    


                                    GPIO.output(water_nose_pin,1)
                                    sleep(0.5)
                                GPIO.output(water_nose_pin,0) 
                                
                                #-----------------------------------
                          
                                
                        #-----------------------                 
                        
                        if "water" == "{}".format(ex[0]) and "mouth" == "{}".format(ex[2]) :
                            
                            
                            #nasal_fluid_motor
                           
                            
                            for x in range(1,6):
                              
                                
                          
                        
                                if "{}".format(ex[1]) == "1":
                              
                                    

                                    
                                    GPIO.output(water_mouth_pin,1)
                                    sleep(0.5)
                                    
                                GPIO.output(water_mouth_pin,0)
                               
                               
                               
                        if "blood" == "{}".format(ex[0]) and "mouth" == "{}".format(ex[2]) :
                            
                            
                            #nasal_fluid_motor
                           
                            
                            for x in range(1,6):
                              
                                
                          
                        
                                if "{}".format(ex[1]) == "1":
                              
                                    

                                    
                                    GPIO.output(blood_mouth_pin,1)
                                    sleep(0.5)
                                    
                                GPIO.output(blood_mouth_pin,0)
                                
                                
                                
                        if "blood" == "{}".format(ex[0]) and "nose" == "{}".format(ex[2]) :
                            
                            
                            #nasal_fluid_motor
                           
                            
                            for x in range(1,6):
                              
                                
                          
                        
                                if "{}".format(ex[1]) == "1":
                              
                                    

                                    
                                    GPIO.output(blood_nose_pin,1)
                                    sleep(0.5)
                                    
                                GPIO.output(blood_nose_pin,0)
                                #-----------------------                 
                        if "heat" == "{}".format(ex[0]) and "body" == "{}".format(ex[2]) :
                            
                            
                            #nasal_fluid_motor
                           
                            
                            for x in range(1,50):
                              
                                
                          
                        
                                if "{}".format(ex[1]) == "1":
                              
                                    

                                    
                                    GPIO.output(heating_pin,1)
                                    sleep(0.5)
                                    
                                GPIO.output(heating_pin,0)
                                
                        if "move" == "{}".format(ex[0]) and "body" == "{}".format(ex[2]) :
                            
                            
                            #move_hand_motor
                           
                            
                            for x in range(1,6):
                                convulsion_motor.start(2.5)
                                
                            
                                if "{}".format(ex[1]) == "-1":
                                        
                                        
                                    
                                        
                                    GPIO.output(convulsion_dir1_pin,1)
                                    
                                    convulsion_motor.ChangeDutyCycle(12) 
                                    sleep(2) 

                                       
                                

                                    
                        
                                if "{}".format(ex[1]) == "1":
                              
                                    

                                    
                                    GPIO.output(convulsion_dir1_pin,1)
                                    convulsion_motor.ChangeDutyCycle(50) 
                                    sleep(.5)   
                                    
                                
                                    
                                GPIO.output(convulsion_dir1_pin,0)
                                convulsion_motor.ChangeDutyCycle(0)  
                    sleep(1)
                    n=n+1
                    print(n)
            n=0
           
                
                
                




        #continue ----------->------------------------------------------------
           

        ##make a disease
        if "make disease" in result_of_talk_array[0]:
            
            final_text = result_of_talk_array[0].split()
            final_text.remove("make")
            final_text.remove("disease")
           
            results = cur.execute("SELECT nameofsymp,state,place FROM blocks WHERE effector='{}' ".format("{}".format(final_text[0])))
            for res in results.fetchall():

    
                result = cur.execute(" UPDATE quistions_db SET activate_state='{}', place='{}'  WHERE nameofsymp='{}' and state='{}' ".format(
                    "a", "{}".format(res[2]), "{}".format(res[0]), "{}".format(res[1])))
                con.commit()
        # if ask a question : 
        final_results = []
        sumition = 0
        results6 = cur.execute("SELECT question FROM quistions_db")
        questions_tube = []
        for res6 in results6.fetchall():
            questions_tube.append(res6[0])

        
        final_data = unique(questions_tube)
        if result_of_talk_array[0] in final_data:

            results7 = cur.execute(
                "SELECT answer,activate_state FROM quistions_db WHERE question='{}'  ".format("{}".format(result_of_talk_array[0])))
            compare_tube = []
            for res7 in results7.fetchall():

                compare_tube.append(res7)
            n = 0
            
            count = 0

            #ttt tube

            for comp in compare_tube:
                count=count+1
                

                if comp[1] == "n":
                    n = n+1
               
                if n == 3:
                    results8 = cur.execute(
                        "SELECT answer,place FROM quistions_db WHERE question='{}' and state='0'  ".format("{}".format(result_of_talk_array[0])))
                    for res8 in results8.fetchall():
                            if " ((organ))" in res8[0]:
                                    jeckvoice("{}".format(res8[0]).replace(
                                        "((organ))", "{}".format(res8[1])))
                            else:
                                jeckvoice(("{}".format(res8[0])))
                    break
                
                 
            if n < 3: 
                #if 1
                results9 = cur.execute(
                    "SELECT answer,state,place FROM quistions_db WHERE question='{}' and activate_state='a'   ".format("{}".format(result_of_talk_array[0])))
                for res9 in results9.fetchall():
              
                    
                            
                    if "((organ))" in res9[0]:
                            jeckvoice("{}".format(res9[0]).replace("((organ))", "{}".format(res9[2])))
                    if "((organ))" not in res9[0]:
                            jeckvoice(("{}".format(res9[0])))
                    break
        

                
            
        # ---------------- > end 
        ##give a drug
        if "take drug" in result_of_talk_array[0]:

            final_text = result_of_talk_array[0].split()
            final_text.remove("take")
            final_text.remove("drug")
            jeckvoice("ok doctor thanks ..... i will take {} ............and tell you what habbened".format(final_text[0]))
            
            from orders import *
            take_drug(final_text[0])

## for now its make disease and give a treatement






    
    


def install_pips():
    #install these lib
    #pip install pipwin
    #pipwin install pyaudio
    #pip install sklearn
    # pip install numpy
    #pip install speech_recognition as sr
    #pip install pyttsx3
    #pip install  easygui
    #sudo apt install espeak

    return 0
