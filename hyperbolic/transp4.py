#!/usr/bin/python3
import numpy as np
from math import exp

# Grid size
m=128
u=np.empty((m+2))
v=np.empty((m+2))
w=np.empty((m+2))
snaps=100
iters=20
z=np.empty((m+2,snaps+1))

# PDE-related constants
c=0.1
dx=1.0/(m+1)
dt=0.005
nu=c*dt/dx

# Initial condition
def f(x):
    return exp(-160*(x-0.85)**2)

# Set up initial condition at timestep 0 and timestep -1
for i in range(m+2):
    x=dx*i
    u[i]=f(x)
    w[i]=f(x-dt)
u[0]=0;w[0]=0
z[:,0]=u

# Integrate the PDE using the leapfrog method
for i in range(1,snaps+1):
    for k in range(iters):

        # Use NumPy routines on all m+2 entries to begin with
        v[:]=w-nu*(np.roll(u,-1)-np.roll(u,1))

        # Overwrite zeroth entry with boundary condition
        v[0]=0

        # Overwrite (m+1)th entry with one-sided finite difference
        v[m+1]=u[m+1]-nu*(u[m+1]-u[m])

        # Cycle pointers to the three arrays
        y=w;w=u;u=v;v=y
    z[:,i]=u

# Output results
for j in range(m+2):
    e=[str(j*dx)]
    for i in range(snaps+1):
        e.append(str(z[j,i]))
    print(" ".join(e))
