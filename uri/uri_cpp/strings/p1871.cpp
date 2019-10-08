#include <iostream>
#include <sstream>
#include <string>
#include <stdlib.h>
#include <stdio.h>

using namespace std;

int main()
{
    long long a, b, c, d = 0, i = 10;

    cin >> a;
    cin >> b;

    while (a != 0 && b != 0) {
        c = a+b;
        while (i <= c*10) {
            if (c % i != 0) {
                d += c % i;
                c -= c % i;
                i*=10;
            } else {
                c/=10;
            }
        }
        cout << d << endl;
        d = 0;
        i = 10;
        cin >> a;
        cin >> b;
    }

    return 0;
}
