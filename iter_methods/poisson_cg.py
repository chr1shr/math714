import numpy as np
import scipy.sparse as sp
import sys
import matplotlib.pyplot as plt

# Grid size and grid spacing
n=51
h=1/(n-1)

# Generate the centered difference differentiation matrix for the Laplacian
de=1/(h*h)
nn=n-2
cen=np.ones(nn*nn)*(4*de)
hor=np.ones(nn*nn-1)*(-de)
ver=np.ones(nn*(nn-1))*(-de)
for i in range(nn-1):
    hor[(i+1)*nn-1]=0
A=sp.diags([cen,hor,hor,ver,ver],[0,1,-1,nn,-nn])

# Right hand side: a vector of ones
rhs=np.ones(nn*nn)
norm_rhs=np.linalg.norm(rhs)

# Solve for solution using the conjugate gradient method
TOL=1.e-4
u_k=np.zeros(nn*nn)
r_k=rhs
p_k=r_k
count=1
while True:

    # First half of conjugate gradient iteration
    w_k=A*p_k
    alpha_k=np.dot(r_k.T,r_k)/np.dot(p_k.T,w_k)
    u_k=u_k+alpha_k*p_k
    r_k_old=r_k
    r_k=r_k-alpha_k*w_k

    # Compute relative residual and use to it to check for convergence
    rel_residual=np.linalg.norm(r_k)/norm_rhs
    print("iteration=%d, relative residual=%g" % (count,rel_residual))
    if rel_residual<TOL:
        break

    # Second half of conjugate gradient iteration
    beta_k=np.dot(r_k.T,r_k)/np.dot(r_k_old.T,r_k_old)
    p_k=r_k+beta_k*p_k
    count+=1

# Print grid spacing and condition number. This may get very expensive for a
# large grid, since it uses a dense linear algebra routine to compute the
# condition number.
print("h=%g, condition number=%g\n" % (h,np.linalg.cond(A.todense())))

# Assemble solution in a grid
uu=np.zeros((n,n))
for i in range(nn):
    for j in range(nn):
        uu[i+1,j+1]=u_k[i+nn*j]

# Plot the solution
xa=np.linspace(0,1,n)
mgx,mgy=np.meshgrid(xa,xa);
ax=plt.figure().add_subplot(projection='3d')
surf=ax.plot_surface(mgx,mgy,uu,rstride=1,cstride=1,cmap=plt.cm.PuOr_r)
ax.set(xlabel='x',ylabel='y',zlabel='z')
plt.show()
