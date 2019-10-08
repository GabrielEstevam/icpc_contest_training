#include <iostream>
#include <sstream>
#include <string>
#include <stdlib.h>
#include <stdio.h>

using namespace std;

void mergeSort (int * numeros, int inicio, int fim);
void intercala (int * numeros, int inicio_a, int fim_a, int inicio_b, int fim_b);

int cont = 0;

int main() {
	int N, entry, s, i;
	s = scanf("%d", &N);
	while (N > 0) {
		int * vetor = (int*)malloc(sizeof(int)*N);
		for (i = 0; i < N; i++) {
			s = scanf("%d", & entry);
			vetor[i] = entry;
		}
		cont = 0;
		mergeSort(vetor, 0, N-1);
		if (cont/2 % 2 == 0) {
			printf("Carlos\n");
		} else {
			printf("Marcelo\n");
		}
		s = scanf("%d", &N);
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
    int i = inicio_a;
    int a, b;
    a = inicio_a;
    b = inicio_b;
    while (a <= fim_a && b <= fim_b) {
        if (numeros[a] <= numeros[b]) {
            aux[i-inicio_a] = numeros[a];
            if (a-i > 0)
        		cont += (a-i);
        	else
        		cont += (i-a);
        	i++;
        	a++;
        } else {
        	if (b-i > 0)
        		cont += (b-i);
        	else
        		cont += (i-b);
            aux[i-inicio_a] = numeros[b];
            i++;
            b++;
        }
    }

    while (a <= fim_a) {
        aux[i-inicio_a] = numeros[a];
        if (a-i > 0)
    		cont += (a-i);
    	else
    		cont += (i-a);
        i++;
        a++;
    }
    while (b <= fim_b) {
        aux[i-inicio_a] = numeros[b];
        if (b-i > 0)
    		cont += (b-i);
    	else
    		cont += (i-b);
    	i++;
    	b++;
    }
    i -= inicio_a;
    for (i = 0; i < (fim_b-inicio_a)+1; i++)
        numeros[inicio_a+i] = aux[i];
}
