#!/usr/bin/python3
import numpy as np
from math import pi,cos,sin,exp
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt


# Calculates the error of the Poisson equation in several different norms
def poisson_error(m):
    mm=m*m
    h=1.0/(m+1)

    # Create derivative matrix and source term
    d=np.zeros((mm,mm))
    f=np.empty((mm))
    hfac=1/(h*h)
    for j in range(m):
        y=(j+1)*h
        for i in range(m):
            ij=j*m+i

            # Construct 5-point Laplacian stencil 
            d[ij,ij]=-4*hfac
            if i>0: d[ij,ij-1]=hfac
            if i<m-1: d[ij,ij+1]=hfac
            if j>0: d[ij,ij-m]=hfac
            if j<m-1: d[ij,ij+m]=hfac

            # Source term
            x=(i+1)*h
            f[ij]=exp(x*y)*(2*pi*(x-1)*x*x*cos(pi*y) \
                          +(2-2*y+x*((-1+x)*(-pi*pi+x*x)+4*y+(-1+x)*y*y))*sin(pi*y))

    # Solve the linear system
    u=np.linalg.solve(d,f)

    # Compute global error by subtracting the analytical solution 
    for j in range(m):
        y=(j+1)*h
        for i in range(m):
            x=(i+1)*h
            u[j*m+i]-=x*(x-1)*exp(x*y)*sin(pi*y)

    # Return 2-norm and infinity norm
    print(m,h,h*np.linalg.norm(u),np.linalg.norm(u,np.inf))

# Calculate the error for a range of grid sizes
for m in (7,15,31,63,95):
    poisson_error(m)
