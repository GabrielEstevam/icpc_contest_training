#include <iostream>
#include <sstream>
#include <string>
#include <stdlib.h>
#include <stdio.h>
#include <math.h>
#include <vector>

using namespace std;

int main() {
    long T, M, N, largura, i, j, soma;
    vector <long> table;
    vector <long> aux;

    cin >> T;
    cin >> M;
    cin >> N;

    largura = N-M+1;

    if (largura == 2) {
        cout << 2 << endl;
    } else if (largura > 2) {
        for (i = 0; i < largura; i++) {
            aux.push_back(1);
            table.push_back(1);
        }
        for (i = 0; i < T-1; i++) {
            for (j = 0; j < largura; j++) {
                if (j == 0)
                    table[j] = aux[j+1];
                else if (j == (largura - 1))
                    table[j] = aux[j-1];
                else
                    table[j] = aux[j-1] + aux[j+1];
            }
            for (j = 0; j < largura; j++)
                aux[j] = table[j]%1000000007;
        }
        soma = 0;
        for (i = 0; i < largura; i++) {
            soma += aux[i] % 1000000007;
        }
        cout << soma % 1000000007 << endl;
    } else {
        cout << 0 << endl;
    }

    return 0;
}
