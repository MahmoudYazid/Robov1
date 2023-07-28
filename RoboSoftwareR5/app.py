import tkinter as tk
from tkinter import ttk
from datetime import datetime

from view.ListApi import *
from model.ModulesImportApi import *
from model.DrugDiseaseInteractionApi import *
from model.ResetAPI import *
from datetime import datetime
from model.SoundApi import *
from model.Variable import *
from model.AnalysisApi import *
from model.ShowMeSympApi import *
from model.Ecg import *


class Ui_MainWindow:
    def __init__(self, root):
        self.root = root
        root.title("RobotikV1")
        root.geometry("900x500")
        root.minsize(900, 600)
        root.maxsize(900, 600)
        root.configure(bg="white")

        self.setup_ui()

    def setup_ui(self):
        self.grid_frame = tk.Frame(self.root, bg="white")
        self.grid_frame.place(x=390, y=0, width=561, height=1000)

        self.AnalysisBtm = ttk.Button(
            self.grid_frame, text="Analysis", style="TButton", command=self.F_AnalysisBtm, width=50)
        self.AnalysisBtm.grid(row=7, column=0, padx=5, pady=5)

        self.pushBtm = ttk.Button(
            self.grid_frame, text="push", style="TButton", command=self.F_PushBtm , width=50)
        self.pushBtm.grid(row=3, column=0, padx=5, pady=5)

        self.EffectorComboBox = ttk.Combobox(
            self.grid_frame, values=QlistUniqueValue)
        self.EffectorComboBox.grid(row=2, column=0, padx=5, pady=5)

        self.resetBtm = ttk.Button(
            self.grid_frame, text="reset", style="TButton", command=self.F_ResetBtm , width=50)
        self.resetBtm.grid(row=5, column=0, padx=5, pady=5)

        self.ECGBTM = ttk.Button(
            self.grid_frame, text="OPEN ECG", style="TButton", command=self.F_OPENECG , width=50)
        self.ECGBTM.grid(row=8, column=0, padx=5, pady=5)

        self.ordersScreenList = tk.Listbox(self.grid_frame, bg="white",width=60)
        self.ordersScreenList.grid(row=0, column=0, rowspan=2, padx=5, pady=5)

        self.tellmeBtm = ttk.Button(
            self.grid_frame, text="tell me", style="TButton", command=self.F_TellMeBtm , width=50)
        self.tellmeBtm.grid(row=4, column=0, padx=5, pady=5)

        self.ShowmeBtm = ttk.Button(
            self.grid_frame, text="Show me", style="TButton", command=self.F_ShowMeBtm , width=50)
        self.ShowmeBtm.grid(row=6, column=0, padx=5, pady=5)
       
        self.robotik_label = tk.Label(
            self.grid_frame, text="Robotik - Robotikeg.com - clinical simulation models industry ", font=("Helvetica", 10))
        self.robotik_label.grid(row=10, column=0, columnspan=2, pady=20)
        


        self.AnalysisScreenList = tk.Listbox(self.root, bg="white")
        self.AnalysisScreenList.place(x=0, y=0, width=391, height=351 )

        self.statusbar = tk.Label(
            self.root, text="", bd=1, relief=tk.SUNKEN, anchor=tk.W)
        self.statusbar.pack(side=tk.BOTTOM, fill=tk.X)

    def F_PushBtm(self):
        self.ordersScreenList.insert(tk.END, "{} You Push Effector {} ....".format(
            datetime.now(), self.EffectorComboBox.get()))
        InterAct(self.EffectorComboBox.get())
        self.ordersScreenList.insert(
            tk.END, "{} Add Done".format(datetime.now()))

    def F_AnalysisBtm(self):
        AutoCheck(self)

    def F_ShowMeBtm(self):
        self.ordersScreenList.insert(
            tk.END, "{} Show me the Symptom Order".format(datetime.now()))
        self.ordersScreenList.insert(
            tk.END, "{} Show me the Symptom Order Done".format(datetime.now()))
        F_ShowMeTheSym()

    def F_OPENECG(self):
        self.ordersScreenList.insert(
            tk.END, "{} OPEN ECG ORDER".format(datetime.now()))
        self.ordersScreenList.insert(
            tk.END, "{} OPEN ECG ORDER".format(datetime.now()))
        openEcg()

    def F_TellMeBtm(self):
        self.ordersScreenList.insert(
            tk.END, "{} Tell me the feeling order".format(datetime.now()))
        self.ordersScreenList.insert(tk.END, tell_Me_the_Feeling())

    def F_ResetBtm(self):
        F_Reset()
        self.ordersScreenList.insert(
            tk.END, "{} Reset Done".format(datetime.now()))


if __name__ == "__main__":
    root = tk.Tk()
    ui = Ui_MainWindow(root)
    root.mainloop()
