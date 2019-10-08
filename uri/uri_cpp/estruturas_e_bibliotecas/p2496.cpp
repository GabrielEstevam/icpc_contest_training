#include <iostream>
#include <sstream>
#include <string>
#include <stdlib.h>
#include <stdio.h>

using namespace std;

void mergeSort (int * numeros, int inicio, int fim);
void intercala (int * numeros, int inicio_a, int fim_a, int inicio_b, int fim_b);

int main()
{
    int instancias, i, j, k = 0, tamanho;
    string entrada;
    int * numerico;

    cin >> instancias;
    for (i = 0; i < instancias; i++) {
        cin >> tamanho;
        cin >> entrada;
        numerico = (int*)malloc(sizeof(int)*tamanho);
        for (j = 0; j < tamanho; j++) {
            numerico[j] = toascii(entrada[j]);
        }
        mergeSort(numerico, 0, tamanho-1);
        for (j = 0; j < tamanho; j++) {
            if (numerico[j] != entrada[j])
                k++;
            if (k == 3) {
                cout << "There aren't the chance." << endl;
                break;
            }
        }
        if (k < 3)
            cout << "There are the chance." << endl;
        k = 0;
        free(numerico);
    }

    return 0;
}

void mergeSort (int * numeros, int inicio, int fim) {
    if (fim - inicio > 1) {
        mergeSort(numeros, inicio, (inicio+fim)/2);
        mergeSort(numeros, (inicio+fim)/2+1, fim);
    }
    intercala(numeros, inicio, (inicio+fim)/2, (inicio+fim)/2+1, fim);
}

void intercala (int * numeros, int inicio_a, int fim_a, int inicio_b, int fim_b) {
    int * aux = (int*)malloc(sizeof(int)*(fim_b-inicio_a+1));
    int i = 0;
    int a, b;
    a = inicio_a;
    b = inicio_b;
    while (a <= fim_a && b <= fim_b) {
        if (numeros[a] <= numeros[b])
            aux[i++] = numeros[a++];
        else
            aux[i++] = numeros[b++];
    }
    while (a <= fim_a)
        aux[i++] = numeros[a++];
    while (b <= fim_b)
        aux[i++] = numeros[b++];
    for (i = 0; i < (fim_b-inicio_a)+1; i++)
        numeros[inicio_a+i] = aux[i];
    free(aux);
}
