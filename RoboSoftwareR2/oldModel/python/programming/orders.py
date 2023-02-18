import sqlite3 as sqlite
from pylinks import *
import pyttsx3
connect= sqlite.connect(sql_db_link)

drug_symp_arr=[]
active_symp_arr=[]
def get_drug_id(name):
    start_connect_get_drug_id=connect.cursor()
    get_id_result=start_connect_get_drug_id.execute(" SELECT effector_id FROM blocks WHERE effector='{}'".format(name))
    for get_id_fetch in get_id_result.fetchall():
        return get_id_fetch[0]

    return 0

def get_id_info(id):
    start_connect_get_id_info = connect.cursor()
    get_id_info_result = start_connect_get_id_info.execute(" SELECT nameofsymp,state FROM blocks WHERE effector_id='{}'".format(id))
    for get_id_info_fetch in get_id_info_result.fetchall():
        add_to_2darray_drug_symp_arr(get_id_info_fetch[0],get_id_info_fetch[1])




    return 0
def add_to_2darray_drug_symp_arr(first_dim_data,second_dim_data):
    drug_symp_arr.append([first_dim_data,int(second_dim_data)])
    return 0

def add_to_2darray_active_symp_arr(first_dim_data,second_dim_data):

    active_symp_arr.append([first_dim_data,int(second_dim_data)])
    return 0

def get_active_symp_info():
    start_connect_get_active_symp_info = connect.cursor()
    get_active_symp_info_result = start_connect_get_active_symp_info.execute(" SELECT nameofsymp,state FROM quistions_db WHERE activate_state='{}'".format("a"))
    for get_active_symp_info_result_fetch in get_active_symp_info_result.fetchall():
        add_to_2darray_active_symp_arr(get_active_symp_info_result_fetch[0],get_active_symp_info_result_fetch[1])


    return 0

def check_inverse_function():
    for active_symp_arr_data_block in active_symp_arr:

        if [active_symp_arr_data_block[0],active_symp_arr_data_block[1]*-1] in drug_symp_arr :
            change(database_name="quistions_db",change_parameter="activate_state",data="n",where_PARAMETER="nameofsymp",where_PARAMETER_EQUAL="{}".format(active_symp_arr_data_block[0]) )

    return 0
def calculation():
    check_inverse_function()

    return 0


def change(database_name,change_parameter,data,where_PARAMETER,where_PARAMETER_EQUAL):
    start_connect_change = connect.cursor()
    get_active_symp_info_result = start_connect_change.execute(
        """
        UPDATE {} SET  {}='{}' WHERE {}='{}'
        
        """.format(database_name,change_parameter,data,where_PARAMETER,where_PARAMETER_EQUAL))

    connect.commit()


    return 0

def check_adverse_drug_effect():
    get_active_symp_info()
    if len(active_symp_arr)==0:
        jeckvoice("no adverse effect of drugs habben in this model doctor")
        return 1
    else:
        return 0

def jeckvoice(text):
    text=text.split()
    if len(text) >7:
        t_ = []
        new_text = ""
        print(text[7])
        for n in range(len(text[7])):
            if "." == text[7][n] or "_" == text[7][n]:
                t_.append(" ")
            else:
                t_.append(text[7][n])

        for x in range(len(t_)):
            new_text = new_text + t_[x]

        print(new_text)
        text[7]=new_text

    engine = pyttsx3.init()
    speed=100
    engine.setProperty("rate", speed)
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[3].id)

    # say method on the engine that passing input text to be spoken
    engine.say("{}".format(text))

    # run and wait method, it processes the voice commands.
    engine.runAndWait()
    return 0
def take_drug(name_drug):
    if check_adverse_drug_effect()==0:
        id_result=get_drug_id(name=name_drug)
        get_id_info(id=id_result)
        calculation()
        active_symp_arr.clear()
        drug_symp_arr.clear()
    return 0



