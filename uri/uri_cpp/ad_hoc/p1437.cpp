#include <iostream>
#include <sstream>
#include <string>
#include <stdlib.h>
#include <stdio.h>

using namespace std;

int main()
{
    int instancias, i, direcao = 0;
    //char entrada[1000];
    char entrada;

    cin >> instancias;
    while (instancias > 0) {
        direcao = 0;
        for (i = 0; i < instancias; i++) {
            cin >> entrada;
            if (entrada == 'D') {
                direcao++;
            } else if (entrada == 'E') {
                direcao+=3;
            }
        }
        direcao = direcao % 4;
        switch (direcao) {
            case 0:
                cout << "N" << endl;
                break;
            case 1:
                cout << "L" << endl;
                break;
            case 2:
                cout << "S" << endl;
                break;
            case 3:
                cout << "O" << endl;
                break;
        }
        cin >> instancias;
    }

    return 0;
}
