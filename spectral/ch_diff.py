#!/usr/bin/python3
from math import *
import matplotlib.pyplot as plt
import numpy as np
from cheb_matrix import cheb

# Function to interpolate
def f(x):
    return 1/(1+5*x*x)

# Analytical derivative
def df(x):
    return -10*x/(1+5*x*x)**2

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
n=24
(xp,D)=cheb(n)
yp=np.array([f(q) for q in xp])

# Sample points
xx=np.linspace(-1,1,500)
yy=np.array([lagr(q,xp,yp) for q in xx])
yy1=np.array([f(q) for q in xx])

# Plot function and Chebyshev interpolant 
plt.figure()
plt.plot(xx,yy,label='Interpolant')
plt.plot(xx,yy1,label='Function')
plt.plot(xp,yp,'o',label='Points')
plt.legend()
plt.xlabel('x')
plt.ylabel('y')
plt.show()

# Compute spectral derivative
dyp=np.dot(D,yp)
dyy=np.array([lagr(q,xp,dyp) for q in xx])
dyy1=np.array([df(q) for q in xx])

# Plot analytical derivative and spectral derivative
plt.figure()
plt.plot(xx,dyy,label='Spectral deriv.')
plt.plot(xx,dyy1,label='Analytical deriv.')
plt.plot(xp,dyp,'o',label='Points')
plt.legend()
plt.xlabel('x')
plt.ylabel('y')
plt.show()
