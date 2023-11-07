#!/usr/bin/python3
import numpy as np
from math import exp,pi,sin
import sys

# Grid size
m=256
u=np.empty((m))
v=np.empty((m))
snaps=64
iters=20
z=np.empty((m,snaps+1))

# Initial condition
def f(x):
    if x>0.1 and x<0.6:
        return 1
    else:
        return 0

# PDE-related constants
A=1.0
dx=1.0/m
dt=0.2*dx

# Set up initial condition
for i in range(m):
    u[i]=f(dx*i)
z[:,0]=u

# Define ENO2 operation
def eno2(a,b,c,d):
    if abs(a-2*b+c)<abs(b-2*c+d):
        return 3*c-4*b+a
    else:
        return d-b

# Integrate the equation
f=0.5*A*dt/dx
for i in range(1,snaps+1):
    for k in range(iters):
        ua=np.roll(u,2)
        ub=np.roll(u,1)
        ud=np.roll(u,-1)
        for j in range(m):
            v[j]=u[j]-f*eno2(ua[j],ub[j],u[j],ud[j])
        u,v=v,u
    z[:,i]=u

# Output results
for j in range(m):
    e=[str(j*dx)]
    for i in range(snaps+1):
        e.append(str(z[j,i]))
    print(" ".join(e))

