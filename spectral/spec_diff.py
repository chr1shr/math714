#!/usr/bin/python3
import matplotlib.pyplot as plt
import numpy as np
from math import *
from scipy.linalg import circulant
import sys

if len(sys.argv)!=2:
    print("Syntax: ./diff.py <mode>\n\n" \
          "mode=1 for order 2 centered-difference\n"
          "mode=2 for order 4 centered-difference\n"
          "mode=3 for spectral")
    sys.exit()

# Function to consider
def f(z):
    return 0.2*cos(z)+1/(2+cos(2*z))

# Derivative
def df(z):
    return -0.2*sin(z)+2*sin(2*z)/(2+cos(2*z))**2

# Differentiation matrix
n=100
h=2*pi/n
if sys.argv[1]=="1" or sys.argv[1]=="2":
    d=np.zeros((n))

    if sys.argv[1]=="1":
        d[1]=-0.5/h
        d[-1]=0.5/h
    else:
        d[2]=1/(12*h)
        d[1]=-2/(3*h)
        d[-1]=2/(3*h)
        d[-2]=-1/(12*h)
elif sys.argv[1]=="3":
    d=np.empty((n))
    d[0]=0
    
    for l in range(1,n):
        d[l]=0.5*(-1)**l/tan(l*h/2)
D=circulant(d)

# Look at the fixed matrix
plt.spy(D)
plt.show()

# Plot function
x=np.linspace(0,2*pi,n,endpoint=False)
y=np.array([f(xx) for xx in x])
plt.xlabel('x')
plt.ylabel('f(x)')
plt.plot(x,y)
plt.show()

# Calculate derivative and plot
dy=np.dot(D,y)
dya=np.array([df(xx) for xx in x])
plt.xlabel('x')
plt.plot(x,dy,label="f' numerical")
plt.plot(x,dya,label="f' analytical")
plt.legend()
plt.show()

# Plot error
err=np.array([dy[i] - df(x[i]) for i in range(n)])
plt.xlabel('x')
plt.ylabel('Derivative error')
plt.plot(x,err)
plt.show()
