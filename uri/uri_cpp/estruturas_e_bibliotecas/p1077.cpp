#include <iostream>
#include <sstream>
#include <string>
#include <stdlib.h>
#include <stdio.h>

using namespace std;

string infixaPosfixa(string infixa);

int main() {
    int instancias;
    string entrada;

    int i;

    cin >> instancias;
    for (i = 0; i < instancias; i++) {
        cin >> entrada;
        cout << infixaPosfixa(entrada) << endl;
    }

    return 0;
}

string infixaPosfixa(string infixa) {
    int i, n = 0, topo = 0, k = 0;
    n = infixa.size();
    char * posfixa = (char*)malloc(sizeof(char)*n);
    char * pilha = (char*)malloc(sizeof(char)*n);

    infixa += ')';
    pilha[topo++] = '(';
    for (i = 0; i < n+1; i++) {
        switch (infixa[i]) {
            case '(':
                    pilha[topo++] = infixa[i];
                    break;
            case ')':
                    while (pilha[topo-1] != '(') {
                        posfixa[k++] = pilha[--topo];
                    }
                    topo--;
                    break;
            case '+':
            case '-':
                    while (pilha[topo-1] != '(') {
                        posfixa[k++] = pilha[--topo];
                    }
                    pilha[topo++] = infixa[i];
                    break;
            case '*':
            case '/':
                    while (pilha[topo-1] != '(' && pilha[topo-1] != '+'  && pilha[topo-1] != '-') {
                        posfixa[k++] = pilha[--topo];
                    }
                    pilha[topo++] = infixa[i];
                    break;
            case '^':
                    while (pilha[topo-1] != '(' && pilha[topo-1] != '+'  && pilha[topo-1] != '-' && pilha[topo-1] != '*' && pilha[topo-1] != '/') {
                        posfixa[k++] = pilha[--topo];
                    }
                    pilha[topo++] = infixa[i];
                    break;
            default:
                    posfixa[k++] = infixa[i];
      }
    }

    string retorno = "";
    for (i = 0; i < k; i++)
        retorno += posfixa[i];
    return retorno;
}
