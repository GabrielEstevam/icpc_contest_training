#include <iostream>
#include <sstream>
#include <string>
#include <stdlib.h>
#include <stdio.h>

using namespace std;

int main()
{
    int instancias, k, i, j, maior = 0;
    string alfabeto = "abcdefghijklmnopqrstuvwxyz";
    int letras[] = {0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0};
    string linha;

    cin >> instancias;
    cin.ignore();
    for (k = 0; k < instancias; k++) {
        getline(cin, linha);
        for (i = 0; i < linha.size(); i++) {
            if (isalpha(linha[i])) {
                for (j = 0; j < 26; j++) {
                    if (tolower(linha[i]) == alfabeto[j])
                        letras[j]++;
                }
            }
        }
        for (i = 0; i < 26; i++) {
            if (letras[i] > maior)
                maior = letras[i];
        }
        for (i = 0; i < 26; i++) {
            if (letras[i] == maior)
                cout << alfabeto[i];
            letras[i] = 0;
        }
        maior = 0;
        cout << endl;
    }

    return 0;
}
