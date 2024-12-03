import numpy as np
from math import pi,cos,sin
from time import time

# Number of FFTs to perform
reps=10000

# Function to consider
def f(z):
    return sin(z)+0*1/(2+cos(2*z))

# Function to evaluate the time taken to perform a fast Fourier
# transform (FFT) on a grid with n points
def fft_time(n):
    x=np.linspace(0,2*pi,n,endpoint=False)
    y=np.array([f(xx) for xx in x])

    # Perform a number of FFT calculations, in order to get better
    # timing statistics
    t0=time()
    for q in range(reps):
        z=np.fft.fft(y)
    return (time()-t0)/reps

# Loop over a range of grid sizes and measure the timen take to
# perform the FFT, reported in microseconds
for n in range(2000,2101):
    print(n,fft_time(n)*1e6)
