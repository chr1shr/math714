#!/usr/bin/python3
import numpy as np
from math import exp,pi,sin
import sys

# Print syntax message
if len(sys.argv)!=2:
    print("Syntax: ./limiters <mode>\n\n" \
          "mode=0 for minmod\n" \
          "mode=1 for superbee")
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

# Define minmod and maxmod functions, used for slope limiter calculations
def minmod(a,b):
    if a*b<=0: return 0
    elif abs(a)<abs(b): return a
    else: return b
def maxmod(a,b):
    if a*b<=0:return 0
    elif abs(a)<abs(b): return b
    else: return a

# Integrate the equation
f=A*dt/dx
for i in range(1,snaps+1):
    for k in range(iters):

        # Compute limited slopes
        sl=(u-np.roll(u,1))
        sr=np.roll(sl,-1)
        if sys.argv[1]=="0":

            # Minmod limiters
            for j in range(m):
                sl[j]=minmod(sl[j],sr[j])
        elif sys.argv[1]=="1":

            # Superbee limiters
            for j in range(m):
                sl[j]=maxmod(minmod(2*sr[j],sl[j]),minmod(sr[j],2*sl[j]))

        else:
            print("Unknown mode")
            sys.exit()

        # Compute update using the limited slopes
        v[:]=u+f*(np.roll(u,1)-u)-0.5*f*(1-f)*(sl-np.roll(sl,1))
        u,v=v,u
    z[:,i]=u

# Output results
for j in range(m):
    e=[str(j*dx)]
    for i in range(snaps+1):
        e.append(str(z[j,i]))
    print(" ".join(e))

