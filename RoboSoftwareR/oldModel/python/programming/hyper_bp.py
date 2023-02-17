import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


last_x=0
last_y=0
cycle_no=0
y_hypo=[0,0,1,1,-1,.5,.5,-5,7,8,9,-.5,-2]

fig = plt.figure(figsize=(6, 6))
x = [0]
y = [0]

ln,= plt.plot(x, y, '-')
plt.axis([0, 100, 0, 10])

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
animation = FuncAnimation(fig, update_hyper_bp, interval=100)
plt.show()
