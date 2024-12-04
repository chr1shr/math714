import numpy as np
from math import pi,cos,sin

# Function to take real part and clean up rounding error. In all examples that
# are passed to this function, the imaginary part is small and can be
# neglected.
def clean(w):
    v=np.real(w)
    for i in range(n):
        if abs(v[i])<1e-15: v[i]=0
    return v

# Consider a discretized function with a small, even number of points
n=6

# Set up function as a sawtooth wave, oscillating between -1 and 1
y=np.array([(-1)**m for m in range(n)])
print("Function values:\n",y)

# Get wave numbers of each mode. Note that the n/2 entry is set as -n/2, which
# creates a small loss in symmetry, as it could equally be n/2. The 1./n
# argument is just an arbitrary grid spacing, to get integers for the wave
# numbers.
wa=np.fft.fftfreq(n,1./n)
print("\nWave numbers:\n",wa);

# Compute the complex FFT in the z array
z=np.fft.fft(y)
print("\nFFT:\n",z)

# Compute first derivative *without* zeroing the n/2 term
dz=z*wa
dy=np.fft.ifft(dz)
print("\nA. Derivative (no zeroing n/2):\n",clean(dy))

# Compute first derivative *with* zeroing the n/2 term
dz[n//2]=0
dy=np.fft.ifft(dz)
print("\nB. Derivative (zeroing n/2):\n",clean(dy))

# Compute second derivative *without* zeroing the n/2 term
d2z=z*np.square(wa)
d2y=np.fft.ifft(d2z)
print("\nC. Second derivative (no zeroing n/2):\n",clean(d2y))

# Compute second derivative *with* zeroing the n/2 term
d2z[n//2]=0
d2y=np.fft.ifft(d2z)
print("\nD. Second derivative (with zeroing n/2):\n",clean(d2y))

