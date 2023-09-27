#!/usr/bin/python3
from math import *
import numpy as np
import matplotlib.pyplot as plt
import sys

# Matrix and vector
A=np.array([[3,0.8],[0.8,1.2]])
#A=np.array([[2,0],[0,2]])       # Alternative best case: circle
f=np.array([4,6])

# Initial guess and tolerance level 
u=np.array([0,0])
eps=1e-10

# Storage for solutions
max_iters=100
u_k=np.empty((100,2))
u_k[0,:]=u

# Steepest descent algorithm
r=f-np.dot(A,u)
k=1
while True:

    # Steepest descent algorithm steps
    w=np.dot(A,r)
    a=np.dot(r,r)/np.dot(r.T,w)
    u=u+a*r
    r=r-a*w

    # Store current solution
    u_k[k,:]=u

    # Check for too many iterations
    if k>100:
        print("Too many iterations")
        sys.exit()

    # Check for convergence
    k+=1
    if np.linalg.norm(r)<eps:
        break        

# Plot results - create contours of phi function
n=100
xx=np.linspace(-4,6,n)
yy=np.linspace(-2,8,n)
X,Y=np.meshgrid(xx,yy)
pxy=np.zeros((n,n))
for i in range(n):
    for j in range(n):
        u=np.array([X[i,j],Y[i,j]])
        pxy[i,j]=0.5*np.dot(u.T,np.dot(A,u))-np.dot(u,f)
plt.contourf(X,Y,pxy,16,alpha=.75)
C = plt.contour(X,Y,pxy,16,colors='black')

# Plot results: overlay progress of algorithm
plt.xlabel('x')
plt.ylabel('y')
plt.plot(u_k[:k,0],u_k[:k,1],color='black')
plt.show()
