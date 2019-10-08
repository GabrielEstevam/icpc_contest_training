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
    string frase;
    int i, j, tamanho;

    cin >> instancias;

    for (i = 0; i < instancias; i++) {
        fflush(stdin);
        getline(cin, entrada);
        tamanho = entrada.size();
        for (j = 0; j < tamanho/2; j++) {
            frase += entrada[tamanho/2 - j - 1];
        }
        for (j = tamanho/2; j < tamanho; j++) {
            frase += entrada[3*tamanho/2 - j - 1];
        }
        cout << frase << endl;
        frase = "";
    }

    return 0;
}
