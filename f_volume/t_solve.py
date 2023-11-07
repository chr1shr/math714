#!/usr/bin/python3
import numpy as np
from math import exp,pi,sin
import sys

# Grid size
m=256
u=np.empty((m))
F=np.empty((m))
v=np.empty((m))
snaps=64
iters=20
z=np.empty((m,snaps+1))

# Initial condition
def f(x):
    if x>0.25 and x<0.75:
        return 0.8
    else:
        return 0

# PDE-related constants
dx=1.0/m
dt=0.2*dx

# Set up initial condition
for i in range(m):
    u[i]=f(dx*i)
z[:,0]=u

# Define flux function
def flux(x):
    return x*(1-x)

# Integrate the equation
f=dt/dx
for i in range(1,snaps+1):
    for k in range(iters):

        # Compute fluxes by solving the Riemann problem
        ul=np.roll(u,1)
        for j in range(m):
            if ul[j]>=0.5 and u[j]<0.5:
                F[j]=0.25
            else:
                Fu=flux(u[j])
                Ful=flux(ul[j])
                if (Fu-Ful<0 and u[j]-ul[j]>0) or \
                   (Fu-Ful>0 and u[j]-ul[j]<0):
                    F[j]=Fu
                else:
                    F[j]=Ful

        # Compute update using the fluxes 
        v[:]=u-f*(np.roll(F,-1)-F)
        u,v=v,u
    z[:,i]=u

# Output results
for j in range(m):
    e=[str(j*dx)]
    for i in range(snaps+1):
        e.append(str(z[j,i]))
    print(" ".join(e))

