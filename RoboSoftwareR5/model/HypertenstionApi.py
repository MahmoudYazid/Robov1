import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from model.DbContext import *


def HypertenstionMainApi():
    InstanseQDB = GeneralConnection.execute(
        "SELECT * FROM QDB WHERE nameofsymp='BP' AND state='1' ")
    for item in InstanseQDB:
        InstanseADB=GeneralConnection.execute(
    "SELECT * FROM ADB WHERE state='1' AND KindId='{}' ".format(item[TablesSchima['QDB']['KindId']]))

        if len([CheckExist for CheckExist in InstanseADB]) > 0:
            x = [x for x in range(0, 200)]

            y = [x for y in range(0, 20) for x in [0, .1, 0, .1, .5, -.5, 0, 0, 0,0]]

        
          


            plt.plot(x, y, label='ECG')
            plt.xlabel('Time (seconds)')
            plt.ylabel('Amplitude')
            plt.title('Synthetic ECG Signal')
            plt.legend()
            plt.grid(True)
            plt.show()


