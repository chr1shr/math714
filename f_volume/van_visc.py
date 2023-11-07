#!/usr/bin/python3
import numpy as np
from math import exp,pi,cos
import sys

# Grid size
m=1024
u=np.empty((m))
v=np.empty((m))
snaps=64
iters=200
z=np.empty((m,snaps+1))

# Initial condition
def f(x):
    return exp(-2-2*cos(2*pi*x))

# PDE-related constants
A=1.0
epsilon=10**(-2.5)
dx=1.0/m
dt=0.06*dx

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
nu=epsilon*dt/(dx*dx)
for i in range(1,snaps+1):
    for k in range(iters):
        ua=np.roll(u,2)
        ub=np.roll(u,1)
        ud=np.roll(u,-1)

        # Compute update from viscous term
        v[:]=(1-2*nu)*u+nu*(ub+ud)

        # Compute nonlinear advection term using ENO2 method
        for j in range(m):
            v[j]-=f*(1-2*u[j])*eno2(ua[j],ub[j],u[j],ud[j])
        u,v=v,u
    z[:,i]=u

# Output results
for j in range(m):
    e=[str(j*dx)]
    for i in range(snaps+1):
        e.append(str(z[j,i]))
    print(" ".join(e))

