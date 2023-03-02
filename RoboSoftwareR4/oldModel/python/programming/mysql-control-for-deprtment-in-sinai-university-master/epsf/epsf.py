import tkinter as  tk

import sqlite3 as mysql
import easygui as gui
from tkinter import ttk
#design
link_db="/home/pi/Desktop/python/programming/jack db.db"
name_of_element_to_change = ["nameofsymp",
                             "effector", "state", "place", "type_effector"]
##func
main=tk.Tk()
main.geometry("2000x2000")
def insert():
    if name.get()=="" or id.get()=="" or email.get()=="" or phone.get()=="" or address.get()=="":
        gui.msgbox(title="Alert",msg="information missing")
        return 0
    con=mysql.connect(database=link_db)
    exe=con.cursor()
    exe.execute("""INSERT INTO blocks(place,effector,nameofsymp,state,type_effector) VALUES ("%s","%s","%s","%s","%s") """ % (
        name.get(), id.get(), email.get(), phone.get(), address.get()))
    con.commit()
def findthis():
    if f_d.get()=="" :
        gui.msgbox(title="Alert",msg="the find text is empty")
        return 0
    con = mysql.connect(database=link_db)
    exe = con.cursor()
    exe.execute(""" SELECT * FROM blocks WHERE effector="%s"  """ %
                (f_d.get()))
    result=exe.fetchall()
    tree = ttk.Treeview(columns=("nameofsymp", "effector", "state", "place", "type_effector"))
    
    def dys():
        tree.destroy()


    btm=tk.Button(text="delete this result", command=dys).place(x=0,y=450)
    for row in result:
        
        tree.heading("{}".format(name_of_element_to_change[0]), text="{}".format(name_of_element_to_change[0]))
        tree.heading("{}".format(name_of_element_to_change[1]),text="{}".format(name_of_element_to_change[1]))
        tree.heading("{}".format(name_of_element_to_change[2]), text="{}".format(name_of_element_to_change[2]))
        tree.heading("{}".format(name_of_element_to_change[3]), text="{}".format(name_of_element_to_change[3]))
        tree.heading("{}".format(name_of_element_to_change[4]), text="{}".format(name_of_element_to_change[4]))
        tree.insert(parent="",index=0,value=(row[0],row[1],row[2],row[3],row[4]))
        tree.place(x=0,y=500)

        con.close()
def remove():
    
    if f_d.get()=="":
        gui.msgbox(title="Alert",msg="missing information")
        return 0
    con = mysql.connect(database=link_db)
    exe = con.cursor()
    exe.execute("""DELETE FROM `blocks` WHERE `effector` ="%s" """ % (f_d.get()))
    con.commit()
    gui.msgbox(title="Alert",msg="delete done")
    con.close()
def modify():
    if change.get()=="" or value.get()=="" or id_mod.get()=="":
        gui.msgbox(title="Alert",msg="information missing")
        return 0

    con = mysql.connect(database=link_db)
    exe = con.cursor()
    exe.execute(""" UPDATE blocks SET `%s`="%s"  WHERE effector="%s"   """ % (change.get(),value.get(),id_mod.get()))
    con.commit()
    gui.msgbox("modify done")
    con.close()


main.title("jack blacks modification")

tk.Label(height=100 ).pack(expand=True)

##new commer
items = []
con = mysql.connect(database=link_db)
exe = con.cursor()
res = exe.execute("SELECT nameofsymp FROM quistions_db ")
for x in res.fetchall():
    if x[0] not in items:

        items.append(x[0])

tk.Label(text="add new symptoms",font=20,border=0).place(x=790,y=0)
tk.Label(text="symptoms \n {}".format([x for x in items]), font=20, border=0).place(x=400, y=300)
#email

tk.Label(text="{}".format(name_of_element_to_change[0]),font=30,border=0).place(x=690,y=50)
email=tk.Entry(width=20,font=33)
email.bind("<Return>",insert)
email.place(x=800,y=50)
#id
tk.Label(text=name_of_element_to_change[1],font=30,border=0).place(x=690,y=100)
id = tk.Entry(width=20,font=33)
id.bind("<Return>",insert)
id.place(x=800,y=100)
##phone
tk.Label(text=name_of_element_to_change[2],font=30,border=0).place(x=690,y=150)
phone=tk.Entry(width=20,font=33)
phone.bind("<Return>",insert)
phone.place(x=800,y=150)
#name
tk.Label(text=name_of_element_to_change[3],font=30,border=0).place(x=690,y=200)
name=tk.Entry(width=20,font=33)
name.bind("<Return>",insert)
name.place(x=800,y=200)
# address
tk.Label(text=name_of_element_to_change[4],font=30,border=0).place(x=690,y=250)
address=tk.Entry(width=20,font=33)
address.bind("<Return>",insert)
address.place(x=800,y=250)
#btm

tk.Button(text="insert", border=0, command=insert).place(x=800, y=400)
###############
#find\delete
tk.Label(text="[ find / delete ]",font=30,bg="white").place(x=140,y=0)
tk.Label(text="name of effector",font=30).place(x=140,y=50)
f_d = tk.Entry(width=20,font=33)
f_d.bind("<Return>",findthis)
f_d.bind("<Return>",remove)
f_d.place(x=100,y=100)

#find
tk.Button(text="find",border=0,command=findthis).place(x=100,y=150)

#delete

tk.Button(text="delete",border=0,command=remove).place(x=200,y=150)
##########
##### modify

tk.Label(text="options",font=30,border=0).place(x=1250,y=0)
# id_mod
tk.Label(text="name of effector",font=30,border=0).place(x=1250,y=30)
id_mod=tk.Entry(width=20,font=33)
id_mod.bind("<Return>",modify)
id_mod.place(x=1200,y=60)
#what to change
tk.Label(text="what do u want to change",font=30,border=0).place(x=1200,y=90)
change=tk.Entry(width=20,font=33)
change.bind("<Return>",modify)
change.place(x=1200,y=120)
#value
tk.Label(text="to value",font=30,border=0).place(x=1250,y=150)
value=tk.Entry(width=20,font=33)
value.bind("<Return>",modify)
value.place(x=1200,y=180)
tk.Button(text="mod",border=0,command=modify).place(x=1230,y=210)


main.mainloop()
