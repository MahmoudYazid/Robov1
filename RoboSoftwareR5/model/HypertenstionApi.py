
from model.DbContext import *
import tkinter as tk
from tkinter import ttk
import plotly.express as px
import plotly.graph_objects as go

def HypertenstionMainApi():
    InstanseQDB = GeneralConnection.execute(
        "SELECT * FROM QDB WHERE nameofsymp='BP' AND state='1' ")
    for item in InstanseQDB:
        InstanseADB=GeneralConnection.execute(
    "SELECT * FROM ADB WHERE state='1' AND KindId='{}' ".format(item[TablesSchima['QDB']['KindId']]))

        if len([CheckExist for CheckExist in InstanseADB]) > 0:
            
         
            xinput = [x for x in range(0, 200)]

            yinput = [x for y in range(0, 20) for x in [0, .1, 0, .1, .5, -.5, 0, 0, 0,0]]
            fig = go.Figure(data=go.Scatter(
            x=xinput,
            y=yinput
        
            ))
            fig.show()


