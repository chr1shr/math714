#!/usr/bin/python3
from math import exp,sin,cos
import numpy as np

# Method:
# 0: stable
# 1: exponentially unstable
# 2: algebraically unstable
method=0

# Total steps
M=101

# Function right hand side
def fun(t,u):
    return sin(t)-u

# Exact solution
def u_exact(t):
    return 0.5*(sin(t)-cos(t))+1.5*exp(-t)

# Step size, and arrays for solution
k=10/(M-1)
t=np.linspace(0,10,M)
f=np.empty((M))
u=np.empty((M))

# Populate the first few entries with the exact solution
u[0:3]=[u_exact(z) for z in t[0:3]]
f[0:3]=[fun(t[i],u[i]) for i in range(0,3)]

# Perform the steps of the method
for n in range(0,M-3):

    if method==0:
        u[n+3]=(u[n+2]+k*(9*sin(t[n+3])+19*f[n+2]-5*f[n+1]+f[n])/24) \
               /(1+9*k/24)

    elif method==1:
        u[n+3]=(-27*u[n+2]+27*u[n+1]+11*u[n] \
               +3*k*(sin(t[n+3])+9*f[n+2]+9*f[n+1]+f[n])) \
               /(11+3*k)
    else:
        u[n+3]=-u[n+2]+u[n+1]+u[n]+2*k*(f[n+2]+f[n+1])
    f[n+3]=fun(t[n+3],u[n+3])

# Output the results
for n in range(0,M):
    ue=u_exact(t[n])
    print(t[n],u[n],f[n],ue,u[n]-ue)

