#!/usr/bin/python3
import tkinter as tk
import tkinter.ttk as ttk
from view.ListApi import *


class GuiWidget(ttk.Labelframe):
    
    def __init__(self, master=None, **kw):
        super(GuiWidget, self).__init__(master, **kw)
        
        self.ChoicesListComponent = ttk.Combobox(self)
        self.ChoicesListComponent.configure(
             width=100, values=QlistUniqueValue)
        self.ChoicesListComponent.grid(
            column=0, row=1)

        
        self.GiveBtn = ttk.Button(self, command=self.insert)
        self.GiveBtn.configure(state="normal", text='Give', width=20)
        self.GiveBtn.grid(column=0, padx=200, pady=10, row=10, sticky="sw")

        self.label2 = ttk.Label(self)
        self.label2.configure(text='Choose drug or disease\n')
        self.label2.grid(column=0, row=0)


        self.ShowMeBtn = ttk.Button(self)
        self.ShowMeBtn.configure(state="normal", text='Show me ', width=30)
        self.ShowMeBtn.grid(column=0, padx=0, pady=10, row=10, sticky="sw")
        
        
        self.ResetBtn = ttk.Button(self)
        self.ResetBtn.configure(state="normal", text='reset', width=20)
        self.ResetBtn.grid(column=0, padx=340, pady=10, row=10, sticky="sw")
        
        
        self.ShowScreenComponant = tk.Text(self)
        self.ShowScreenComponant.configure(
            height=10,
            setgrid="false",
            state="normal",
            tabstyle="tabular",
            width=100)
        self.ShowScreenComponant.grid(column=0, row=4)
        
        self.configure(height=200, text='Main\n', width=200)
        self.pack(side="top")
        
       

    
    def ResetScreen(self):
        self.ShowScreenComponant.delete('1.0',tk.END)
        for data in ShowScreenList:
           
            self.ShowScreenComponant.insert("1.0", " - ")
        
    
 
    def insert(self):
        self.ShowScreenComponant.insert("1.0", "{}".format(data))
        
        
        self.ShowScreenComponant.after(100, self.ResetScreen)
        
        
        
        
        






if __name__ == "__main__":



    while True:
        root = tk.Tk()

        widget = GuiWidget(root)
        
        widget.pack(expand=True, fill="both")
    

        root.mainloop()
        


