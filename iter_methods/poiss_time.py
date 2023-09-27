#!/usr/bin/python3
import numpy as np
from time import time,process_time
from math import pi,cos,sin,exp

# Replicates the computation in poisson2.py, and measures the time for
# computation, as well as the memory in the matrix. Since this routine uses
# dense linear algebra, it scales very poorly, and is only designed to be run
# with small grids. The code illustrates why it is necessary to develop methods
# for efficiently solving sparse linear systems like this.
def poisson_time(m):
    mm=m*m
    h=1.0/(m+1)

    # Get the current time(), a measure of "wall-clock time", the physical
    # passage of time as you would observe by looking at a wall clock
    t0=time()

    # Get the current process_time(), a measure of the time that this program
    # has actually spent on the processor
    p0=process_time()

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

    # Return the elapsed time, using both the time() routine and the
    # process_time() routine, plus the memory allocation of the matrix
    return (time()-t0,process_time()-p0,d.size*d.itemsize)

# Calculate the error for a range of grid sizes
m=7
m+=m//7
while m<250:
    (ttotal,ptotal,mem)=poisson_time(m)
    print(m,ttotal,ptotal,mem)
    m+=m//7
