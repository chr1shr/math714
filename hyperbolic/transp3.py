#!/usr/bin/python3
import numpy as np
from math import *

# Grid size
m=64

def acc(m):

    # Initialize solution array and constants
    u=np.empty((m))
    c=0.1
    dx=1.0/m
    dt=dx

    # Diffusion constant, scaled with grid spacing. (Change to 0.5*c*c*dx for
    # Lax-Wendroff.)
    b=0.02*dx

    # Stencil entries combining advection and diffusion
    nu=0.5*c*dt/dx
    mu=b*dt/(dx*dx)
    d0=nu+mu
    d1=1-2*mu
    d2=-nu+mu

    # Initial condition
    for j in range(m):
        x=dx*j
        u[j]=exp(-3*cos(2*pi*x))

    # Integrate for one time unit
    for k in range(m):
        u[:]=d0*np.roll(u,1)+d1*u[:]+d2*np.roll(u,-1)

    # Calculate L2 norm to exact solution (without diffusion)
    err=0
    for j in range(m):
        x=dx*j
        du=u[j]-exp(-3*cos(2*pi*(x-c)))
        err+=du*du
    return sqrt(dx*err)

# Loop over a range of grid sizes
m=16
while m<=3100:

    # Print the number of grid points, the grid spacing, and the L2 norm
    print(m,1.0/m,acc(m))

    # Increase grid points by 50%
    m+=m//2
