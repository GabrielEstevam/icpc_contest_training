#include <iostream>
#include <sstream>
#include <string>
#include <stdlib.h>
#include <stdio.h>

using namespace std;

void mergeSort (int * numeros, int inicio, int fim);
void intercala (int * numeros, int inicio_a, int fim_a, int inicio_b, int fim_b);
int * copia (int * original, int tamanho);
void imprime_fila (int * fila, int tamanho);

int main()
{
    int instancias, i, j, k = 0, tamanho;
    int * fila, * fila_ordenada;

    cin >> instancias;
    for (i = 0; i < instancias; i++) {
        cin >> tamanho;
        fila = (int*)malloc(sizeof(int)*tamanho);
        for (j = 0; j < tamanho; j++) {
            cin >> fila[j];
        }
        fila_ordenada = copia(fila, tamanho);
        mergeSort(fila_ordenada, 0, tamanho-1);
        for (j = 0; j < tamanho; j++) {
            if (fila_ordenada[tamanho-1-j] == fila[j])
                k++;
        }
        cout << k << endl;
        k = 0;
        free(fila);
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
}

int * copia (int * original, int tamanho) {
    int * copia;
    int i;
    copia = (int*)malloc(sizeof(int)*tamanho);
    for (i = 0; i < tamanho; i++)
        copia[i] = original[i];
    return copia;
}

void imprime_fila (int * fila, int tamanho) {
    int i;
    for (i = 0; i < tamanho; i++) {
        cout << "|" << fila[i] << "|";
    }
    cout << endl;
}
