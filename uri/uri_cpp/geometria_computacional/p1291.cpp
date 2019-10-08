#include <iostream>
#include <sstream>
#include <string>
#include <stdlib.h>
#include <stdio.h>
#include <math.h>
 
using namespace std;
 
int main() {
	double r, a, b, c;
	double coef = 1 - (asin(0.5) + 0.5*sqrt(0.75));
	//long double coef2 = 1 - (asin(0.5) + 0.5*sqrt(0.75));

	while (cin >> r) {
		c = r*r*coef;
        	b = r*r*(1 - M_PI/4) - 2*c;
        	a = r*r - 4*b - 4*c;
		b *= 4;
		c *= 4; 
        	printf("%.3f %.3f %.3f\n", a, b, c);
	}	
 
	return 0;
}
