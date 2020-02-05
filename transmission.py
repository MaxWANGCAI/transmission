import numpy as np
from numpy import matlib as ml
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import random

fig, ax = plt.subplots()

#参数设置
# dim = 400
# original_count = 2
dim = 500
original_count = 5
broad_rate=0.03
shadow_time = 0
hospital_receive_time = 0
bed_count = 0
u = 0.99


def f(x):
    return sum(x.tolist(),[])
    
#生成数据：

s = np.matlib.randn(dim,2)*2
a=["b"]*dim
set = np.concatenate((s, np.matrix(a).reshape(dim,1)),axis=1)
for i in random.sample(range(0,dim),original_count):
    set[i,2]="r"
    
# points = ax.scatter(f(set[:,0]), f(set[:,1]),c=f(set[:,2]),marker=verts)

#传染判定：
def ifbroad(a,b):
    if ((a[0]-b[0])**2+(a[1]-b[1])**2)**0.5<0.3:
        if random.uniform(0,1)<broad_rate:
            return True
    else: return False    
    

def update(t):
    while t<100:
        global u
        y=(1.5**u-0.5)*np.matlib.randn(dim,2)/10
        global set
        set = np.concatenate((set[:,0:2].astype('float64')+y,set[:,2]),axis=1)         
        #传染：
        for i in range(0,dim-1):
            for j in range(i+1,dim-1):
                if set[i,2] != set[j,2]:
                    if ifbroad(f(set[i,0:2].astype('float64')),f(set[j,0:2].astype('float64'))) == True:
                        set[i,2]="r"
                        set[j,2]="r"
        xdata = f(set[:,0].astype('float64'))
        ydata = f(set[:,1].astype('float64'))
        color = f(set[:,2])
        plt.cla()
        points = ax.scatter(xdata, ydata,c=color)
        return points,

ani = FuncAnimation(fig, update,frames=range(0,100) ,interval = 1)
plt.show()
