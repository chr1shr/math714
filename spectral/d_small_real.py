import numpy as np

# Consider a discretized function with a small, even number of points
n=6

# Set up function as a sawtooth wave, oscillating between -1 and 1
y=np.array([(-1)**m for m in range(n)])
print("Function values:\n",y)

# Compute the real FFT in the z array. This will have n/2+1 complex entries.
# Importantly, because of symmetry, Im(z[0]) and Im(z[n/2]) are ignored. That
# leaves 2*(n/2+1)-2 = n degrees of freedom, matching the input size.
z=np.fft.rfft(y)
print("\nReal FFT:\n",z)

# Compute first derivative *without* zeroing the n/2 term
dz=z*(1j*np.arange(n//2+1))
dy=np.fft.irfft(dz)
print("\nA. Derivative (no zeroing n/2):\n",dy)

# Compute first derivative *with* zeroing the n/2 term
dz[n//2]=0
dy=np.fft.irfft(dz)
print("\nB. Derivative (zeroing n/2):\n",dy)

# Compute second derivative *without* zeroing the n/2 term
d2z=z*(-np.square(np.arange(n//2+1)))
d2y=np.fft.irfft(d2z)
print("\nC. Second derivative (no zeroing n/2):\n",d2y)

# Compute second derivative *with* zeroing the n/2 term
d2z[n//2]=0
d2y=np.fft.irfft(d2z)
print("\nD. Second derivative (with zeroing n/2):\n",d2y)
