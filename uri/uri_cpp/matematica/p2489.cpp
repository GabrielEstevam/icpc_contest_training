#include <iostream>
#include <sstream>
#include <string>
#include <stdlib.h>
#include <stdio.h>
#include <math.h>

using namespace std;

int main() {
    double A, D, R, a;
    double pi = atan(1)*4;
    while (cin >> A) {
        cin >> D;
        cin >> R;
        a = D*cos(R*pi/180);
        printf("%.4f\n", A-a);
    }
    return 0;
}
