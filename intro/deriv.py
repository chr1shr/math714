#!/usr/bin/python3
from math import sin,cos,exp

# Function to numerically differentiate
def f(z):
    return exp(z)*sin(z)

# Initial step size, and position to evaluate the derivative at
h=0.1
x=1

# Exact derivative
dfexact=exp(x)*(cos(x)+sin(x))

while h>1e-10:

    # Compute the derivative using the finite-difference stencil 
    df=(f(x+2*h)+3*f(x)-4*f(x-h))/(6*h)

    # Print the numerical and exact derivatives, and the magnitude of absolute
    # error
    print(h,df,dfexact,abs(df-dfexact))

    # Divide the grid spacing by 10
    h*=0.5
