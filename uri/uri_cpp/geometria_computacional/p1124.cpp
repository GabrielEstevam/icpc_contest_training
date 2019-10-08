#include <iostream>
#include <sstream>
#include <string>
#include <stdlib.h>
#include <stdio.h>
#include <math.h>

using namespace std;

int main()
{
    int L, C, R1, R2;
    int L1, L2;
    int maior = 0, menor = 0;
    double d = 0;

    cin >> L;

    while (L > 0) {
        cin >> C;
        cin >> R1;
        cin >> R2;
        L1 = L-R1-R2;
        L2 = C-R1-R2;
        if (L1 >= 0 && L2 >= 0) {
            d = pow(L1, 2);
            d += pow(L2, 2);
            d = sqrt(d);
        }
        if (R1+R2 <= d) {
            cout << "S" << endl;
        } else {
            if (R1 >= R2) {
                maior = R1;
                menor = R2;
            } else {
                maior = R2;
                menor = R1;
            }
            d = pow(maior, 2);
            d *= 2;
            d = sqrt(d);
            d -= maior;
            if (d >= 2*menor) {
                cout << "S" << endl;
            } else {
                cout << "N" << endl;
            }
        }
        cin >> L;
        d = 0;
    }

    return 0;
}
