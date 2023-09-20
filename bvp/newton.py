#!/usr/bin/python3
from math import sin,cos

# Function to perform root-finding on
def f(x):
    return sin(x)-0.9+x**3

# Analytical derivative
def df(x):
    return cos(x)+3*x*x

# Choose starting point for Newton iteration
xa=1

for k in range(20):

    # Print out the current iterate, and the function value there
    print("%17.10g %17.10g" % (xa,f(xa)))

    # Perform Newton step
    xa=xa-f(xa)/df(xa)
