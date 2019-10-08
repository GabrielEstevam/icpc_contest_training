#include <iostream>
#include <sstream>
#include <string>
#include <stdlib.h>
#include <stdio.h>

using namespace std;

int main()
{
    long long a, b, maior, saida, i;

    while (cin >> a) {
        cin >> b;

        i = 2;
        saida = 0;
        if (a > 0 || b > 0) {
            if (a >= b) {
                maior = a;
            } else {
                maior = b;
            }
            while (maior > 1) {
                maior /= 2;
                i *= 2;
            }
        }

        while (i > 0) {
            if ((a >= i ||  b >= i) && (a < i || b < i)) {
                saida += i;
            }
            if (a >= i) {
                a -= i;
            }
            if (b >= i) {
                b -= i;
            }
            i /= 2;
        }
        cout << saida << endl;

    }

    return 0;
}

