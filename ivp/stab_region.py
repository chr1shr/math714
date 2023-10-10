#!/usr/bin/python3
from math import *
import numpy as np
import matplotlib.pyplot as plt

# Polynomial coefficients
pol=np.array([11,-18,9,-2.],dtype=complex);coeff=6.
#pol=np.array([25,-48,36,-16,3],dtype=complex);coeff=12
#pol=np.array([137,-300,300,-200,75,-12],dtype=complex);coeff=60

# Computes the maximum magnitude of the root of the stability polynomial
# for lambda*h=x+y*i
def f(x,y):
    a=np.copy(pol)
    a[0]-=coeff*(x+1j*y)
    return np.max(np.abs(np.roots(a)))

# Plot results - find the 1 contour of max_r(|z_r(lambda*h)|) function
n=129
xx=np.linspace(-20,20,n)
yy=np.linspace(-20,20,n)
X,Y=np.meshgrid(xx,yy)
pxy=np.empty((n,n))
for i in range(n):
    for j in range(n):
        pxy[j,i]=sqrt(f(xx[i],yy[j]))
plt.contourf(X,Y,pxy,16,alpha=.75)
plt.contour(X,Y,pxy,levels=[1],colors='black')
plt.show()
