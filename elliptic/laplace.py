#!/usr/bin/python3
import numpy as np
from math import pi,cos,sin,exp
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

# Exact solution of the Laplace equation
def u_ex(x,y):
    return cos(3*x)*exp(3*y)

# Calculates the error of the Poisson equation in several different norms
def laplace_error(m):
    m2=m+2;mm=m2*m2
    h=1.0/(m+1)

    # Create derivative matrix, starting with the diagonal terms already
    # present 
    hfac=1/(6*h*h)
    d=np.diag(-20*hfac*np.ones(mm))
    f=np.zeros((mm))
    for j in range(1,m+1):
        y=j*h
        for i in range(1,m+1):
            ij=j*m2+i
            x=i*h

            # Construct 9-point Laplacian stencil 
            d[ij,ij-m2-1]=hfac;
            d[ij,ij-m2]=4*hfac;
            d[ij,ij-m2+1]=hfac;
            d[ij,ij-1]=4*hfac;
            d[ij,ij+1]=4*hfac;
            d[ij,ij+m2-1]=hfac;
            d[ij,ij+m2]=4*hfac;
            d[ij,ij+m2+1]=hfac;

    # Fill in bottom and top Dirichlet conditions
    for i in range(0,m2):
        f[i]=-20*hfac*u_ex(i*h,0)
        f[i+m2*(m+1)]=-20*hfac*u_ex(i*h,1)

    # Fill in the side Dirichlet conditions
    for j in range(1,m+1):
        f[j*m2]=-20*hfac*u_ex(0,j*h)
        f[j*m2+m+1]=-20*hfac*u_ex(1,j*h)

    # Solve the linear system
    u=np.linalg.solve(d,f)

    # Compute global error by subtracting the analytical solution 
    for j in range(m2):
        for i in range(m2):
            u[j*m2+i]-=u_ex(i*h,j*h)

    # Return 2-norm and infinity norm
    print(m,h,h*np.linalg.norm(u),np.linalg.norm(u,np.inf))

#laplace_error(31)

# Calculate the error for a range of grid sizes
for m in (7,15,31,63,95):
    laplace_error(m)
