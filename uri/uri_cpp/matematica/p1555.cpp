#include <iostream>
#include <sstream>
#include <string>
#include <stdlib.h>
#include <stdio.h>
#include <math.h>

using namespace std;

int main()
{
    int instancias, i;
    double x, y, r, b, c;

    cin >> instancias;
    for (i = 0; i < instancias; i++) {
        cin >> x;
        cin >> y;
        r = pow(3*x, 2) + pow(y, 2);
        b = 2*pow(x, 2) + pow(5*y, 2);
        c = 100*x*-1 + pow(y, 3);
        if (r > b && r > c) {
            cout << "Rafael ganhou" << endl;
        } else if (b > r && b > c) {
            cout << "Beto ganhou" << endl;
        } else {
            cout << "Carlos ganhou" << endl;
        }
    }

    return 0;
}
