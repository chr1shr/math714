#include <cstdio>
#include <cstdlib>

#include "matrix.hh"

/** Calculates a random number uniformly distributed in a given range.
 * \param[in] (a,b) the range.
 * \return The computed number. */
inline double rnd(double a,double b) {
    return a+((b-a)/RAND_MAX)*static_cast<double>(rand());
}

/** Creates a rectangular matrix where each entry is uniformly
 * distributed between -1 and 1.
 * \param[in] (m,n) the dimensions of the matrix.
 * \return A pointer to the matrix. */
double* rand_matrix(int m,int n) {
    int mn=m*n;
    double *A=new double[mn];
    for(int i=0;i<mn;i++) A[i]=rnd(-1,1);
    return A;
}

/** Creates a rectangular matrix where each entry is uniformly
 * distributed between -1 and 1.
 * \param[in] (m,n) the dimensions of the matrix.
 * \return A pointer to the matrix. */
double* gradient_matrix(int m,int n) {
    double *A=new double[m*n];
    for(int i=0;i<m;i++) {
        for(int j=0;j<n;j++) {
            A[j+n*i]=j;
        }
    }
    return A;
}

/** Creates a diagonal matrix.
 * \param[in] (m) the dimension of the matrix.
 * \return A pointer to the matrix. */
double* diag_matrix(int m) {
    int mm=m*m;
    double *A=new double[mm];
    for(int i=0;i<mm;i++) A[i]=0;
    for(int i=0;i<m;i++) A[i*(m+1)]=1;
    return A;
}

/** Prints the entries of a rectangular matrix. 
 * \param[in] (m,n) the dimensions of the matrix. */
void print_matrix(double *A,int m,int n) {
    for(int i=0;i<m;i++) {
        printf("%g",A[n*i]);
        for(int j=1;j<n;j++) printf(" %g",A[n*i+j]);
        putchar('\n');
    }
}
