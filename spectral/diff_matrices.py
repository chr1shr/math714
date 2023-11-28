import numpy as np
from scipy.linalg import circulant
from math import *
import sys

# Assembles a differentiation matrix for a period grid of size n on [0,2pi).
def diff_matrix(n,k):

    # Grid spacing
    h=2*pi/n

    # Finite-difference matrices
    if k>0 and k<3:
        d=np.zeros((n))
        if k==1:
            
            # Second-order matrix
            d[1]=-0.5/h
            d[-1]=0.5/h
        else:

            # Fourth-order matrix
            d[2]=1/(12*h)
            d[1]=-2/(3*h)
            d[-1]=2/(3*h)
            d[-2]=-1/(12*h)
            
    elif k==3:

        # Spectral derivative
        d=np.empty((n))
        d[0]=0
        for l in range(1,n):
            d[l]=0.5*(-1)**l/tan(l*h/2)

    else:
        print("Matrix type unknown")
        sys.exit()
    return circulant(d)
