#include <iostream>
#include <sstream>
#include <string>
#include <stdlib.h>
#include <stdio.h>
#include <math.h>

using namespace std;

int main()
{
    float   a, b, c;

    cin >> a;
    cin >> b;
    cin >> c;

    if ((fabs(b-c) < a && a < (b+c)) && (fabs(a-c) < b && b < (a+c)) && (fabs(a-b) < c && c < (a+b))) {
        printf("Perimetro = %.1f\n", (a+b+c));
    } else {
        printf("Area = %.1f\n", (a+b)*c/2);
    }

    return 0;
}

