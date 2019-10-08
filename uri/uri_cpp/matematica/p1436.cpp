#include <iostream>
#include <sstream>
#include <string>
#include <stdlib.h>
#include <stdio.h>
#include <math.h>

using namespace std;

int main()
{
    int instancias, tamanho, entrada, i, j, capitao = 0;

    cin >> instancias;
    for (i = 0; i < instancias; i++) {
        cin >> tamanho;
        for (j = 0; j < tamanho; j++) {
            cin >> entrada;
            if (j == floor(tamanho/2))
                capitao = entrada;
        }
        cout << "Case " << (i+1) << ": " << capitao << endl;
    }

    return 0;
}
