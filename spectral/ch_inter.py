#!/usr/bin/python3
from math import *
import matplotlib.pyplot as plt
import numpy as np

# Function to interpolate
def f(x):
    return exp(-10*x*x)

# Function to evaluate the Lagrange interpolation
def lagr(x,xp,yp):
    lm=0
    for k in range(xp.size):
        xc=xp[k]
        li=1
        for l in range(xp.size):
            if l!=k:
                li*=(x-xp[l])/(xp[k]-xp[l])
        lm+=yp[k]*li
    return lm

# Control points
n=16
xp=np.linspace(-1,1,n+1) # (Linearly spaced)
#xp=np.cos(np.linspace(0,np.pi,n+1))
yp=np.array([f(q) for q in xp])

# Sample points
xx=np.linspace(-1,1,513)
yy=np.array([lagr(q,xp,yp) for q in xx])
yy1=np.array([f(q) for q in xx])

# Plot figure using Matplotlib
plt.figure()
plt.plot(xx,yy,label='Interpolant')
plt.plot(xx,yy1,label='Function')
plt.plot(xp,yp,"o",label='Points')
plt.legend()
plt.xlabel('x')
plt.ylabel('y')
plt.show()
