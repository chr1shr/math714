#!/usr/bin/python3
import numpy as np
from diff_matrices import diff_matrix
from math import *
import sys

# Check for a single command-line argument
if len(sys.argv)!=2:
    print("Syntax: ./diff.py <mode>\n\n" \
          "mode=1 for order 2 centered-difference\n"
          "mode=2 for order 4 centered-difference\n"
          "mode=3 for spectral")
    sys.exit()

# Function to consider
def f(z):
    return 0.2*sin(z)+1/(2+cos(2*z))

# Derivative
def df(z):
    return 0.2*cos(z)+2*sin(2*z)/(2+cos(2*z))**2

# Assemble derivative matrix
def diff_error(n):

    D=diff_matrix(n,int(sys.argv[1]))

    x=np.linspace(0,2*pi,n,endpoint=False)
    y=np.array([f(xx) for xx in x])

    # Calculate derivative and plot
    dy=np.dot(D,y)
    err=np.array([dy[i]-df(x[i]) for i in range(n)])

    return np.linalg.norm(2*pi/n*err)

n=10
while n<30000:
    print(n,2*pi/n,diff_error(n))
    n+=2*(n//4)
