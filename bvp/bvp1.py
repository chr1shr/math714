#!/usr/bin/python3
import numpy as np
from math import *

# Boundary condition values
al=exp(1)
be=exp(-1)

# Set grid resolution
m=49
h=1/(m+1)
x=np.linspace(h,1-h,m)

# Generate the centered difference differentiation matrix for u''
f=1/(h*h)
A=np.diag(-np.ones(m)*f*2)+np.diag(np.ones(m-1)*f,1)+np.diag(np.ones(m-1)*f,-1)

# Define the right-hand side vector
F=np.array([pi*pi*exp(cos(pi*z))*(sin(pi*z)**2-cos(pi*z)) for z in x])

# Modify the first and last entries of F to handle the Dirichlet conditions
F[0]-=al*f
F[m-1]-=be*f

# Solve the linear system
U=np.linalg.solve(A,F)

# Print the exact and approximate solutions, and compute the infinity norm
# error
infnorm=0
for i in range(m):
    uex=exp(cos(pi*x[i]))
    E=U[i]-uex
    if abs(E)>infnorm:
        infnorm=abs(E)
    print(x[i],U[i],uex,E)
print("# Infinity norm error:",infnorm)
