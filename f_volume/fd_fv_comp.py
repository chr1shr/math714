#!/usr/bin/python3
import numpy as np
from math import exp,pi,sin
import sys

# Print syntax message
if len(sys.argv)!=3:
    print("Syntax: ./fd_fv_comp <mode> <output>\n\n" \
          "mode=0 for finite difference\n" \
          "mode=1 for finite volume\n\n"
          "output=0 for solution snapshots\n"
          "output=1 to measure change in integral")
    sys.exit()

# Grid size
m=256
u=np.empty((m))
v=np.empty((m))
r=np.empty((m))
s=np.empty((m))
snaps=100
iters=1000
z=np.empty((m,snaps+1))

# Spatially varying diffusivity
def beta(x):
    return 0.12+0.08*sin(2*pi*x);

# Initial condition
def f(x):
    if x<0.25 or x>0.75:
        return 0
    else:
        return 1

# PDE-related constants
dx=1.0/m
dt=0.3*dx*dx/(0.2*2)
mu=dt/(dx*dx)

# Set up initial condition
for i in range(m):
    u[i]=f(dx*i)
z[:,0]=u

if sys.argv[1]=="0":

    # Initialize r_i and s_i terms in finite difference stencil
    for i in range(m):
        x=dx*i
        A=0.25*(beta(x+dx)-beta(x-dx))
        B=beta(x)
        r[i]=mu*(-A+B)
        s[i]=mu*(A+B)

elif sys.argv[1]=="1":

    # Initialize r_i and s_i terms in finite volume stencil
    for i in range(m):
        x=dx*i
        r[i]=mu*beta(x-0.5*dx)
        s[i]=mu*beta(x+0.5*dx)

else:
    print("Unrecognized mode")
    sys.exit()

# Integrate the PDE
p=1-r-s
for i in range(1,snaps+1):
    for k in range(iters):
        v[:]=p*u+r*np.roll(u,1)+s*np.roll(u,-1)

        # Cycle pointers to the three arrays
        w=u;u=v;v=w
    z[:,i]=u

# Output results
if sys.argv[2]=="0":
    for j in range(m):
        e=[str(j*dx)]
        for i in range(snaps+1):
            e.append(str(z[j,i]))
        print(" ".join(e))

# Output change in integral of solution
elif sys.argv[2]=="1":
    I0=np.sum(z[:,0])
    for j in range(snaps+1):
        print(j,j*dt*iters,dx*(np.sum(z[:,j])-I0))

else:
    print("Output type not recognized")
