#include <iostream>
// this code will compile

double cube(double x) {
	return x*x*x;
}

int main()
{
	double x = 1.2;
	std::cout << cube(x) << std::endl;
	return 0;
}
