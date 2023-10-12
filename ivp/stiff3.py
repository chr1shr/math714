#!/usr/bin/python3
import numpy as np
from math import exp

# Matrices
a=np.array([[998,1998],[-999,-1999]])
i=np.identity(2)

# Initial conditions
ut=np.array([[1],[0]])
ui=np.array([[1],[0]])

# Starting time and timestep (currently chosen within the stability region of
# the explicit method)
t=0
k=0.1

while t<10:

    # Print solutions and exact solution
    ex1=2*exp(-t)-exp(-1000*t)
    ex2=-exp(-t)+exp(-1000*t)
    print(t,ex1,ex2,ut[0,0],ut[1,0],ui[0,0],ui[1,0])

    # Trapezoid step
    tmp=ut+0.5*k*np.dot(a,ut)
    ut=np.linalg.solve(i-0.5*k*a,tmp)

    # Implicit step
    ui=np.linalg.solve(i-k*a,ui)
    t+=k
