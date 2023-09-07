#!/usr/bin/python3
import numpy as np

# Points to use in finite difference stencil
s=[-2,-1,0,1,2]
n=len(s)

# Assemble linear system using the transpose of the Vandermonde matrix
A=np.fliplr(np.vander(s)).T
d=np.zeros((n))
d[1]=1

# Solve the linear system and print the coefficients
b=np.linalg.solve(A,d)
for i in range(len(s)):
    print("Coeff. of f(x + %gh): %g"%(s[i],b[i]))
