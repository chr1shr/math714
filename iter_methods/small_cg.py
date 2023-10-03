import numpy as np

# Total number of grid points, and mesh spacing
n=9
h=1/(n+1)
hfac=1/(h*h)

# Calculates the multiplication Au for a given input vector u, without
# explicitly building the matrix A
def mul_A(u):
    Au=-2*u

    Au[0]+=u[1]
    for i in range(1,n-1): Au[i]+=u[i-1]+u[i+1]
    Au[n-1]+=u[n-2]
    Au*=hfac
    return Au

# Conjugate gradient algorithm
r_k=np.ones((n))
u_k=np.zeros((n))
p_k=np.copy(r_k)
rr=np.dot(r_k,r_k)
print("# 0",rr)
k=1
while k<=n:

    # Update solution by moving in the direction of the p vector
    w_k=mul_A(p_k)
    alpha=rr/np.dot(p_k,w_k)
    u_k+=alpha*p_k
    r_k-=alpha*w_k

    # Compute the 2-norm squared of the residual vector and check
    # for convergence
    new_rr=np.dot(r_k,r_k)
    print("#",k,new_rr)
    if new_rr<1e-20:
        break

    # Compute new conjugate direction p
    beta_k=new_rr/rr
    rr=new_rr
    p_k=r_k+beta_k*p_k
    k+=1

# Print out the solution
print("\n",0,0)
for i in range(0,n):
    print(h*(i+1),u_k[i])
print(1,0)
