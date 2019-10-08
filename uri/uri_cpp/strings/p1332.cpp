#include <iostream>
#include <sstream>
#include <string>
#include <stdlib.h>
#include <stdio.h>

using namespace std;

int main()
{
    int instancias;
    string entrada;
    int i;
    int one = 0, two = 0, three = 0;

    cin >> instancias;
    for (i = 0; i < instancias; i++) {
        cin >> entrada;
        if (entrada.size() == 3) {
            if (entrada[0] == 'o') one++;
            if (entrada[1] == 'n') one++;
            if (entrada[2] == 'e') one++;
            if (entrada[0] == 't') two++;
            if (entrada[1] == 'w') two++;
            if (entrada[2] == 'o') two++;
        } else {
            if (entrada[0] == 't') three++;
            if (entrada[1] == 'h') three++;
            if (entrada[2] == 'r') three++;
            if (entrada[3] == 'e') three++;
            if (entrada[4] == 'e') three++;
        }
        if (one >= 2)
            cout << 1 << endl;
        else if (two >= 2)
            cout << 2 << endl;
        else if (three >= 4)
            cout << 3 << endl;
        one = 0;
        two = 0;
        three = 0;
    }

    return 0;
}
