#include <iostream>
#include <sstream>
#include <string>
#include <stdlib.h>
#include <stdio.h>

using namespace std;

int main()
{
    string entrada;
    char pilha[1000];
    int i, tamanho, topo = -1;

    while (getline(cin,entrada)) {
        tamanho = entrada.size();
        for (i = 0; i < tamanho; i++) {
            if (entrada[i] == ')' && topo >= 0) {
                if (pilha[topo] == '(')
                    topo--;
                else
                    pilha[++topo] = entrada[i];
            } else if (entrada[i] == '(' || entrada[i] == ')') {
                pilha[++topo] = entrada[i];
            }
        }
        if (topo == -1)
            cout << "correct" << endl;
        else
            cout << "incorrect" << endl;
        topo = -1;
    }
    return 0;
}
