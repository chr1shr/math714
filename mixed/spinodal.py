#!/usr/bin/python3
import numpy as np
from math import *
from scipy.sparse import csr_array
import scipy.sparse.linalg as sla
from time import time
import sys
import os

np.set_printoptions(threshold=sys.maxsize)

# Grid size
m=80
mm=m*m
h=1./m
k=h

# Miscellaneous parameters 
beta=3
snaps=200
iters=10

# Initial grid
u=np.random.uniform(-1,1,(m,m))

# Create arrays to assemble sparse matrices
iptr=np.empty((mm+1),dtype=np.int32)
idx=np.empty((5*mm),dtype=np.int32)
dat_i=np.empty((5*mm))
dat_e=np.empty((5*mm))
fac=0.5*k/h*h
cen_i=1+4*fac
cen_e=1-4*fac

for j in range(m):
    for i in range(m):
        l=i+m*j
        iptr[l]=5*l

        # Create list of indices of orthogonal neighbors, taking into account
        # periodicity
        w=[l]
        if j==0: w+=[l-m+mm]
        else: w+=[l-m]
        if i==0: w+=[l-1+m]
        else: w+=[l-1]
        if i==m-1: w+=[l+1-m]
        else: w+=[l+1]
        if j==m-1: w+=[l+m-mm]
        else: w+=[l+m]

        # Sort the list of indices, and add them to the list for assembling the
        # sparse matrices
        w.sort()
        for q in range(5):
            p=5*l+q
            idx[p]=w[q]
            if w[q]==l:
                dat_i[p]=cen_i
                dat_e[p]=cen_e
            else:
                dat_i[p]=-fac
                dat_e[p]=fac
iptr[mm]=5*mm
A_i=csr_array((dat_i,idx,iptr),shape=(mm,mm))
A_e=csr_array((dat_e,idx,iptr),shape=(mm,mm))

# Crank-Nicolson step to integrate the diffusive term over a timestep k
def c_n(u):
    v=A_e.dot(u)
    u[:]=sla.spsolve(A_i,v)

# Explicit step to handle the reaction terms over a timestep k/2
def react(u):
    u[:]+=0.5*beta*k*u*(np.ones(mm)-u*u)

# Outputs the solution in a format that can be read by Gnuplot.
# Type 'splot 'filename' matrix binary'
def gp_matrix(u,filename):
    m=u.shape[0]

    # Create output array with padding for Dirichlet boundary conditions
    # and coordinate ranges
    f=np.zeros((m+1,m+1),dtype=np.float32)
    f[1:,1:]=u

    # Set coordinate ranges
    f[0,0]=m
    f[1:,0]=np.linspace(0,1,m,endpoint=False)
    f[0,1:]=np.linspace(0,1,m,endpoint=False)

    # Output single-precision floating point numbers as a binary data to a file
    f.tofile(filename)


# Create output directory and save first frame
odir="spinodal.odr"
if not os.path.exists(odir):
    os.mkdir(odir)
gp_matrix(u,odir+"/u.0")

# Perform timesteps
u.shape=(mm)
for i in range(1,snaps+1):
    for j in range(iters):

        # Strang splitting
        react(u)
        c_n(u)
        react(u)

    # Save output snapshot, converting data to a grid
    print("# Output frame",i)
    u.shape=(m,m)
    gp_matrix(u,odir+"/u."+str(i))
    u.shape=(mm)
