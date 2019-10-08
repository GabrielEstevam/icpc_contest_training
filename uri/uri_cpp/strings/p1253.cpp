#include <iostream>
#include <sstream>
#include <string>
#include <stdlib.h>
#include <stdio.h>

using namespace std;

int main()
{
    string alfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    string entrada, saida = "";
    int instancias, i, j, k;
    int deslocamento;
    cin >> instancias;
    for (k = 0; k < instancias; k++) {
        cin >> entrada;
        cin >> deslocamento;
        for (i = 0; i < entrada.size(); i++) {
            for (j = 0; j < 26; j++) {
                if (entrada[i] == alfabeto[j]) {
                    if (j-deslocamento < 0)
                        saida += alfabeto[j-deslocamento+26];
                    else
                        saida += alfabeto[j-deslocamento];
                }
            }
        }
        cout << saida << endl;
        saida = "";
    }
    return 0;
}
