import numpy as np
from math import pi,cos,sin
from time import time

# Function to consider
def f(z):
    return sin(z)+0*1/(2+cos(2*z))

# Derivative
def df(z):
    return 0.2*cos(z)+2*sin(2*z)/(2+cos(2*z))**2

def fft_time(n):
    x=np.linspace(0,2*pi,n,endpoint=False)
    y=np.array([f(xx) for xx in x])
    
    t0=time()
    for q in range(10000):
        z=np.fft.fft(y)
    return time()-t0

for n in range(2000,2101):
    print(n,fft_time(n))
