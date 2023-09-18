#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

#include "matrix.hh"

// The minimum length of each timing test in seconds
const double t_dur=1;

// Timing function, return the number of seconds from a specified datum
inline double wtime() {
    return double(clock())/CLOCKS_PER_SEC;
}

int main() {
    double *A;

    // Loop over a range of different matrix sizes to test the computation time
    for(int m=100;m<=3000;m+=100) {

        // Perform as many tests as possible within a fixed duration. This is a
        // useful method to get accurate timing results even for very fast
        // computations, since in that case the time can be averaged over many
        // repeats.
        double t0=wtime(),t1;
        long n=0;
        do {

            // Generate a random m by m matrix and then free the memory
            A=rand_matrix(m,m);
            delete [] A;

            n++;t1=wtime();
        } while(t1<t0+t_dur);

        // Print the timing results, computing the average time for each test
        printf("m = %4d, %8ld tests, %12g ms per test\n",m,n,1e3*(t1-t0)/n);
    }
}
