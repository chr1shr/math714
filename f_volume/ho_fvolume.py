#!/usr/bin/python3
import numpy as np
from math import exp,pi,sin
import sys

# Print syntax message
if len(sys.argv)!=2:
    print("Syntax: ./ho_fvolume <mode> <output>\n\n" \
          "mode=0 for first-order Godunov\n"
          "mode=1 for Lax-Wendroff\n"
          "mode=2 for Beam-Warming")
    sys.exit()

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

# Integrate first-order Godunov method
f=A*dt/dx
if sys.argv[1]=="0":
    for i in range(1,snaps+1):
        for k in range(iters):
            v[:]=u+f*(np.roll(u,1)-u)
            u,v=v,u
        z[:,i]=u

# Lax-Wendroff method
elif sys.argv[1]=="1":
    sl=0.5*f*(1+f)
    sc=1-f*f
    sr=0.5*f*(-1+f)
    for i in range(1,snaps+1):
        for k in range(iters):
            v[:]=sl*np.roll(u,1)+sc*u+sr*np.roll(u,-1)
            u,v=v,u
        z[:,i]=u

# Beam-Warming method
elif sys.argv[1]=="2":
    sll=-0.5*f+0.5*f*f
    sl=f*(2-f)
    sc=1-1.5*f+0.5*f*f
    for i in range(1,snaps+1):
        for k in range(iters):
            v[:]=sll*np.roll(u,2)+sl*np.roll(u,1)+sc*u
            u,v=v,u
        z[:,i]=u

else:
    print("Integration type not known")
    sys.exit()

# Output results
for j in range(m):
    e=[str(j*dx)]
    for i in range(snaps+1):
        e.append(str(z[j,i]))
    print(" ".join(e))

