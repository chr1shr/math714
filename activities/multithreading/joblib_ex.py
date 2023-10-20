import joblib as jl

NUM_THREADS=4

v1=range(1000000)

def happy(n):
    i=0
    while i<1000:
        i+=1
        if n==1: return 0
        if n==4: return 1

        m=n;n=0;
        while m>0:
            d=m%10;m//=10
            n+=d*d
    return 2

fgen=(jl.delayed(happy)(i) for i in range(len(v1)))

v3=jl.Parallel(n_jobs=NUM_THREADS)(fgen)

print(v3)
