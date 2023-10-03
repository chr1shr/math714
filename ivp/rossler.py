#!/usr/bin/python
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# Constants in model
a=0.2
b=0.2
c=5.7

# Function to calculate derivatives x, y, and z in the Rossler attractor
def deriv(x,t):
    return np.array([-x[1]-x[2], \
                     x[0]+a*x[1], \
                     b+x[2]*(x[0]-c)])

# Solve ODE using the "odeint" library in SciPy
time=np.linspace(0,600,20001)
xinit=np.array([-3,0,0])
x=odeint(deriv,xinit,time)

# Code to do a 3D plot
#ax=plt.figure().add_subplot(projection='3d')
#plt.plot(x[5000:,0],x[5000:,1],x[5000:,2])
#plt.show()

# Code to do a 2D plot of x versus y
#plt.plot(x[:,0],x[:,1])
#plt.xlabel('x')
#plt.ylabel('y')
#plt.show()

# Optional section to print out the data
for i in range(10000,20001):
    print(" ".join([str(time[i])]+[str(z) for z in x[i,:]]))
