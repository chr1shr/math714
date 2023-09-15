#include "matrix.hh"

int main() {
    const int m=4;
    double *A=diag_matrix(m);

    print_matrix(A,m,m);
    delete [] A;
}
