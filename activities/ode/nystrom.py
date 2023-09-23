#!/usr/bin/python3
from math import cos,sin,pi
import sys

# Function to integrate
def f(t,y):
    return -y

# Integration interval
L=10

def nystrom(N,output):

    # Initial values for y(0) and y'(0)
    y=0
    dy=1

    # Number of timesteps, and step size
    t=0
    h=L/N
    h2=h*h

    # Apply Euler step until t>2
    if output: print(0,y,dy)
    for i in range(N):

        # Nystrom intermediate steps
        t=i*h
        dk1=f(t,y)
        dk2=f(t+0.5*h,y+0.5*h*dy+h2*0.125*dk1)
        dk3=f(t+h    ,y+    h*dy+h2*  0.5*dk2)

        # Update y and its derivative
        y+=h*dy+h2/6*(dk1+2*dk2)
        dy+=h/6*(dk1+4*dk2+dk3)

        if output: print(t+h,y,dy)

    return (y,dy)

# Run the integrator once and print out the solution
nystrom(200,True)
sys.exit()

# Run the integrator many times to see how the error scales
for N in (16,32,64,128,256,512):
    (y,dy)=nystrom(N,False)
    print(N,L/N,y-sin(L),dy-cos(L))

