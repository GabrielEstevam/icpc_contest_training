#include <iostream>
#include <sstream>
#include <string>
#include <stdlib.h>
#include <stdio.h>

using namespace std;

int main()
{
    int instancias, i, j;
    char entrada;
    char pilha[1000];
    int topo = -1;
    int diamantes = 0;

    cin >> instancias;
    cin.ignore();
    for (i = 0; i < instancias; i++) {
        entrada = getc(stdin);
        while (entrada == '<' || entrada == '.' || entrada == '>') {
            if (entrada == '>' && topo >= 0) {
                if (pilha[topo] == '<') {
                    topo--;
                    diamantes++;
                } else {
                    pilha[++topo] = entrada;
                }
            } else if (entrada != '.') {
                pilha[++topo] = entrada;
            }
            entrada = getc(stdin);
        }
        cout << diamantes << endl;
        diamantes = 0;
        topo = -1;
    }

    return 0;
}
