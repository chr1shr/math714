#!/usr/bin/python3
import numpy as np
from math import pi,cos,sin,exp
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

# Source term for Poisson equation
def ff(x,y):
    return 2*(x-1)*x**3+6*x*(2*x-1)*(y-1)*y

# Calculates the error of the Poisson equation in several different norms
def poisson_error(m):
    mm=m*m
    h=1.0/(m+1)

    # Create derivative matrix and source term
    d=np.zeros((mm,mm))
    f=np.empty((mm))
    hfac=1/(6*h*h)
    for j in range(m):
        y=(j+1)*h
        for i in range(m):
            ij=j*m+i

            # Construct 9-point Laplacian stencil 
            d[ij,ij]=-20*hfac
            if j>0:
                if i>0: d[ij,ij-m-1]=hfac
                d[ij,ij-m]=4*hfac
                if i<m-1: d[ij,ij-m+1]=hfac
            if j<m-1:
                if i>0: d[ij,ij+m-1]=hfac
                d[ij,ij+m]=4*hfac
                if i<m-1: d[ij,ij+m+1]=hfac
            if i>0: d[ij,ij-1]=4*hfac
            d[ij,ij]=-20*hfac
            if i<m-1: d[ij,ij+1]=4*hfac

            # Source term
            x=(i+1)*h
            f[ij]=ff(x,y)
            
            # Correction from nabla^2 f (analytical)
            #f[ij]+=h*h/12*(24*(x*(2*x-1)+(y-1)*y))

            # Correction from nabla^2 f (numerical)
            #f[ij]+=1/12.*(ff(x-h,y)+ff(x+h,y)+ff(x,y-h)+ff(x,y+h)-4*ff(x,y))

    # Solve the linear system
    u=np.linalg.solve(d,f)

    # Compute global error by subtracting the analytical solution 
    for j in range(m):
        y=(j+1)*h
        for i in range(m):
            x=(i+1)*h
            u[j*m+i]-=x*x*x*(x-1)*y*(y-1)

    # Return 2-norm and infinity norm
    print(m,h,h*np.linalg.norm(u),np.linalg.norm(u,np.inf))


# Calculate the error for a range of grid sizes
for m in (7,15,31,63,95):
    poisson_error(m)
