#!/usr/bin/python
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import sys

# Constants in Rossler ODE system
a=0.2
b=0.2
c=5.7

# Maximum number of Newton iterations
max_nsteps=100

# Function to calculate derivatives x, y, and z in the Rossler attractor
def f(U,t):
    return np.array([-U[1]-U[2], \
                     U[0]+a*U[1], \
                     b+U[2]*(U[0]-c)])

# Function F to perform root-finding on, to compute the trapezoid update
# implicitly
def F(U,U_n,t,k):
    return 2*(U_n-U)+k*(f(U_n,t)+f(U,t+k))

# Jacobian of F, required for the Newton iteration
def J_F(U,t,k):
    return np.array([[-2,-k,-k],
                     [k,-2+a*k,0],
                     [k*U[2],0,-2+k*(U[0]-c)]])

# Initial condition, and step size
t=0
U_n=np.array([-3.,0,0])
k=0.02

# Perform timesteps
print(t,U_n[0],U_n[1],U_n[2])
while t<600:

    l=0
    q=0
    U=np.copy(U_n)
    
    # Perform Newton updates until two steps are below a tolerance
    while l<2:

        # Calculate Newton iteration
        F_=F(U,U_n,t,k)
        U-=np.linalg.solve(J_F(U,t,k),F_)

        # Check if the Newton iteration has converged
        if np.linalg.norm(F_)<1e-12: l+=1
        else: l=0
        
        # Check for too many iterations
        q+=1
        if q==max_nsteps:
            print("Too many Newton iterations")
            sys.exit()
    
    # Update solution using the result of the Newton iteration
    U_n=U
    t+=k
    print(t,U_n[0],U_n[1],U_n[2],q)
