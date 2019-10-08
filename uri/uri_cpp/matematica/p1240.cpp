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
    int64_t a, b;
    bool flag = true;

    cin >> instancias;
    for (i = 0; i < instancias; i++) {
        cin >> a;
        cin >> b;
        if (b <= a) {
            while (b > 0) {
                if (a%10 == b%10) {
                    a /= 10;
                    b /= 10;
                } else {
                    flag = false;
                    break;
                }
            }
        } else {
            flag = false;
        }
        if (flag) {
            cout << "encaixa" << endl;
        } else {
            cout << "nao encaixa" << endl;
        }
        flag = true;
    }

    return 0;
}
