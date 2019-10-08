#include <iostream>
#include <sstream>
#include <string>
#include <stdlib.h>
#include <stdio.h>

using namespace std;

int main()
{
    char entrada;
    string saida = "";
    char numero;

    while (true) {
        cin >> numero;
        if (numero == '0')
            break;
        cin.ignore();
        entrada = getc(stdin);
        while (isdigit(entrada)) {
            if (entrada != numero) {
                if (entrada != '0' || saida.size() > 0)
                saida += entrada;
            }
            entrada = getc(stdin);
        }
        if (saida.size() == 0)
            cout << 0 << endl;
        else
            cout << saida << endl;
        saida = "";
    }
    return 0;
}
