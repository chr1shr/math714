#!/usr/bin/python3
from math import sin,cos

# Function to perform root-finding on
def f(x):
    return sin(x)-0.9+x**3

# Analytical derivative
def df(x):
    return cos(x)+3*x*x

# Newton method setup
xa=1

for k in range(20):
    print("%17.10g %17.10g" % (xa,f(xa)))

    # Newton
    xa=xa-f(xa)/df(xa)
