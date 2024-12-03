#!/usr/bin/python3
import numpy as np

# Computes the (n+1) Chebyshev-Lobatto points at the associated derivative
# matrix
def cheb(n):

    # Chebyshev-Lobatto points
    x=np.cos(np.linspace(0,np.pi,n+1))

    # Weighting array
    c=np.ones((n+1))
    c[0]=2
    c[n]=2

    # Set up diagonal terms
    D=np.empty((n+1,n+1))
    D[0,0]=(2*n*n+1)/6
    for i in range(1,n):
        D[i,i]=-0.5*x[i]/(1-x[i]*x[i])
    D[n,n]=-D[0,0]

    # Set up off-diagonal terms
    for i in range(n+1):
        for j in range(n+1):
            if i!=j:
                D[i,j]=c[i]*(-1)**(i+j)/(c[j]*(x[i]-x[j]))
    return (x,D)
