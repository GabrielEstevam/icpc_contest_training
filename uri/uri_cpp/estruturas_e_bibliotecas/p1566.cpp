#include <iostream>
#include <sstream>
#include <string>
#include <stdlib.h>
#include <stdio.h>
#include <algorithm>

using namespace std;

int main()
{
    int instancias, tamanho, numero, i, j;
    int * numeros;

    cin >> instancias;
    for (i = 0; i < instancias; i++) {
        scanf("%d", &tamanho);
        numeros = (int*)malloc(sizeof(int)*tamanho);
        for (j = 0; j < tamanho; j++) {
            scanf("%d", &numero);
            numeros[j] = numero;
        }
        sort(numeros, numeros+tamanho);
        for (j = 0; j < tamanho-1; j++) {
            printf("%d ", numeros[j]);
        }
        printf("%d\n", numeros[tamanho-1]);
        free(numeros);
    }

    return 0;
}
