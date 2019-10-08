#include <iostream>
#include <sstream>
#include <string>
#include <stdlib.h>
#include <stdio.h>

using namespace std;

int reconhecimento (string entrada);
int regra (int a, int b);

int main()
{
    /**
        Entrada:
        1 - pedra
        2 - papel
        3 - tesoura
        4 - lagarto
        5 - spock

        Regras:
        1 e 2 => 2
        1 e 3 => 1
        1 e 4 => 1
        1 e 5 => 5
        2 e 3 => 3
        2 e 4 => 4
        2 e 5 => 2
        3 e 4 => 3
        3 e 5 => 5
        4 e 5 => 4
    **/

    int instancias, i;
    string entrada1, entrada2;
    int a, b, c;

    cin >> instancias;
    for (i = 0; i < instancias; i++) {
        cin >> entrada1;
        cin >> entrada2;
        a = reconhecimento(entrada1);
        b = reconhecimento(entrada2);
        if (a == b) {
            cout << "empate" << endl;
        } else {
            c = regra(a, b);
            if (c == 1)
                cout << "rajesh" << endl;
            else
                cout << "sheldon" << endl;
        }
    }

    return 0;
}

int regra (int a, int b) {
    int c = 0;
    if ((a == 1 && b == 2)||(b == 1 && a == 2))
        c = 2;
    if ((a == 1 && b == 3)||(b == 1 && a == 3))
        c = 1;
    if ((a == 1 && b == 4)||(b == 1 && a == 4))
        c = 1;
    if ((a == 1 && b == 5)||(b == 1 && a == 5))
        c = 5;
    if ((a == 2 && b == 3)||(b == 2 && a == 3))
        c = 3;
    if ((a == 2 && b == 4)||(b == 2 && a == 4))
        c = 4;
    if ((a == 2 && b == 5)||(b == 2 && a == 5))
        c = 2;
    if ((a == 3 && b == 4)||(b == 3 && a == 4))
        c = 3;
    if ((a == 3 && b == 5)||(b == 3 && a == 5))
        c = 5;
    if ((a == 4 && b == 5)||(b == 4 && a == 5))
        c = 4;

    if (c == a)
        return 1;
    else if (c == b)
        return 2;
    else
        return 0;
}

int reconhecimento (string entrada) {
    if (entrada.size() == 5) {
        if (entrada[1] == 'e')
            return 1;
        if (entrada[1] == 'a')
            return 2;
        if (entrada[0] == 's')
            return 5;
    } else {
        if (entrada[0] == 't')
            return 3;
        if (entrada[0] == 'l')
            return 4;
    }
    return 0;
}
