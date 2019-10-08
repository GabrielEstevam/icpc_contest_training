#include <iostream>
#include <sstream>
#include <string>
#include <stdlib.h>
#include <stdio.h>

using namespace std;

int main()
{
    int instancias, i, k = 0;
    float entrada;

    cin >> instancias;
    for (i = 0; i < instancias; i++) {
        cin >> entrada;
        while (entrada > 1) {
            entrada /= 2;
            k++;
        }
        cout << k << " dias" << endl;
        k = 0;
    }

    return 0;
}
