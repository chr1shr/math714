import numpy as np
from math import pi,cos,sin
from time import time

# Number of redundant FFT computations for more accurate timing
fft_comps=10

# Function to consider
def f(z):
    return 0.2*sin(z)+1/(2+cos(2*z))
#    return sin(10*z)
#    return abs(sin(z))

# Derivative
def df(z):
    return 0.2*cos(z)+2*sin(2*z)/(2+cos(2*z))**2
#    return 10*cos(10*z)
#    if z<pi:
#        return cos(z)
#    else:
#        return -cos(z)

# Computes the time taken and the error of the spectral derivative
def spec_diff(n):

    # Set up function vector
    x=np.linspace(0,2*pi,n,endpoint=False)
    y=np.array([f(xx) for xx in x])

    # Record initial wall-clock time
    t0=time()

    # Perform FFT-based spectral derivative
    for j in range(fft_comps):
        z=np.fft.rfft(y)
        z[0:n//2]*=1j*np.arange(n//2)
        z[n//2]=0
        dy=np.fft.irfft(z)

    # Record elapsed wall-clock time
    t0=time()-t0

    # Return computed error at wall-clock time
    err=np.array([dy[i]-df(x[i]) for i in range(n)])
    return (np.linalg.norm(2*pi/n*err),t0/fft_comps)

n=10
while n<100000:
    print(*((n,)+spec_diff(n)))
    n+=2*(n//4)
