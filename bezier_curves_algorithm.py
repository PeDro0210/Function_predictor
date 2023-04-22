import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import make_interp_spline
from matplotlib.path import Path
from matplotlib.patches import PathPatch
import math as math
import numpy as np


x=[]
y=[]

xx=[]
yy=[]

pi=math.pi

def function(x):
    
    return math.sin(x)


for x3 in range(-10,11,1):
    
    #if the range is for real numbers
    # if x3 < 0:
    #     print("negative")
    
    y2=function(x3)
    
    
    x.append(x3)
    y.append(y2)
    


        

intercep = len(x) // 2
refence_point_one = len(x) // 3.5
refence_point_two = len(x) // 7.5

print(f"intercep: {intercep} refence_point_one: {refence_point_one} refence_point_two: {refence_point_two} ")

# After intercep
# each point goes from end to end 

intercep2 = -intercep
reference_point2_one2 = -refence_point_one+len(x)-1
reference_point2_two2 = -refence_point_two+len(x)-1


for i in range(0, len(x)):
    if y[i] == 0 or i == intercep or i == refence_point_one or i == refence_point_two or \
    i == reference_point2_one2 or i == reference_point2_two2  or i == len(x) - 1 or i==0 or i==intercep2:
        
        print(f"i: {i} x: {x[i]} y: {y[i]}")
        xx.append(x[i])
        yy.append(y[i])


   

verts_list = []
codes_list = []
for i in range(0, len(xx) - 1):
    washi=2
    x1, y1 = xx[i], yy[i]
    x2, y2 = xx[i+1], yy[i+1]
    x_mid = (x1 + x2) /washi
    y_mid = (y1 + y2) /washi
    verts = np.array([(x1, y1), (x_mid, y1), (x_mid, y2), (x2, y2)], dtype=float)
    codes = [Path.MOVETO, Path.CURVE4, Path.CURVE4, Path.CURVE4]
    verts_list.append(verts)
    codes_list.append(codes)



fig, ax = plt.subplots()


print("patching the graph")
for verts, codes in zip(verts_list, codes_list):
    path = Path(verts, codes)
    patch = PathPatch(path, facecolor='none', lw=1)
    ax.add_patch(patch)


fig.set_figheight(10)
fig.set_figwidth(10)
ax.plot(x, y)
ax.plot(xx, yy, 'ro', markersize=5)

ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title("Function predictions (IT DOESNT WORK WITH POLINOMIALS AND RATIONALS) ")

plt.show()