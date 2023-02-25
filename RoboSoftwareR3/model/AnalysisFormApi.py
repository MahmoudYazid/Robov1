# This will import all the widgets
# and modules which are available in
# tkinter and ttk module
from tkinter import *
from tkinter.ttk import *

# creates a Tk() object

def AnalysisPage():

	master = Tk()


	# sets the geometry of main
	# root window
	master.geometry("200x200")

	# Toplevel object which will
	# be treated as a new window


	# A Label widget to show in toplevel
	Label(master,
            text=AnalysisText).pack()

