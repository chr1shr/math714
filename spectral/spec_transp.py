#!/usr/bin/python3
import numpy as np
from math import pi,cos,sin

# Number of output snapshots
snaps=40

# Number of iterations per snapshot
iters=32

# Total grid points
n=256
hn=n//2

# Grid spacing a time step size
h=2*pi/n
dt=h/4

# Grid, initial condition, and previous step for use with the leapfrog method
x=np.linspace(0,2*pi,n,endpoint=False)
u=np.exp(-200*(1-np.cos(x-1)))
u_prev=np.exp(-200*(1-np.cos(x-0.2*dt-1)))

# Speed
c=0.2+np.square(np.sin(x-1))

# Spectral derivative
def du(u):
    z=np.fft.rfft(u)
    z[0:hn]*=1j*np.arange(hn)
    z[hn]=0
    return np.fft.irfft(z)

# Store initial snapshot
z=np.empty((n,snaps+1))
z[:,0]=u

for i in range(1,snaps+1):
    for j in range(iters):
        u_x=du(u)

        # Calculate next step
        uu=u_prev-2*dt*c*u_x

        # Update arrays
        u_prev[:]=u;u[:]=uu
    z[:,i]=u

# Print snapshots
for j in range(n):
    e=[str(x[j])]
    for i in range(snaps+1):
        e.append(str(z[j,i]))
    print(" ".join(e))
