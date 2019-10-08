#include <iostream>
#include <sstream>
#include <string>
#include <stdlib.h>
#include <stdio.h>
#include <math.h>

using namespace std;

int ** multiplicao(int ** A, int ** B);
void copia(int ** A, int ** B);
void printMatriz(int ** A);

int main()
{
    int instancias = 0, i, j, n;
    char entrada;
    int *** As;
    int ** A, ** aux, ** mul;

    /* Pre calculo */
    As = (int***)malloc(sizeof(int**)*10);
    As[0] = (int**)malloc(sizeof(int*)*2);
    As[0][0] = (int*)malloc(sizeof(int)*2);
    As[0][1] = (int*)malloc(sizeof(int)*2);
    As[0][0][0] = 1; As[0][0][1] = 0; As[0][1][0] = 0; As[0][1][1] = 1;
    As[1] = (int**)malloc(sizeof(int*)*2);
    As[1][0] = (int*)malloc(sizeof(int)*2);
    As[1][1] = (int*)malloc(sizeof(int)*2);
    As[1][0][0] = 0; As[1][0][1] = 1; As[1][1][0] = 1; As[1][1][1] = 1;

    A = (int**)malloc(sizeof(int*)*2);
    A[0] = (int*)malloc(sizeof(int)*2);
    A[1] = (int*)malloc(sizeof(int)*2);
    A[0][0] = 1; A[1][0] = 0; A[0][1] = 0; A[1][1] = 1;

    for (i = 2; i <= 9; i++)
        As[i] = multiplicao(As[i-1], As[1]);
    /* Fim do pre calculo */

    aux = (int**)malloc(sizeof(int*)*2);
    aux[0] = (int*)malloc(sizeof(int)*2);
    aux[1] = (int*)malloc(sizeof(int)*2);

    mul = (int**)malloc(sizeof(int*)*2);
    mul[0] = (int*)malloc(sizeof(int)*2);
    mul[1] = (int*)malloc(sizeof(int)*2);

    cin >> instancias;
    cin.ignore();
    for (i = 0; i < instancias; i++) {
        scanf("%c", &entrada);
        while (isdigit(entrada)) {
            copia(aux, A);
            for (j = 0; j < 9; j++) {
                mul[0][0] = (A[0][0]*aux[0][0] + A[0][1]*aux[1][0]) % 1000;
                mul[0][1] = (A[0][0]*aux[0][1] + A[0][1]*aux[1][1]) % 1000;
                mul[1][0] = (A[1][0]*aux[0][0] + A[1][1]*aux[1][0]) % 1000;
                mul[1][1] = (A[1][0]*aux[0][1] + A[1][1]*aux[1][1]) % 1000;
                copia(A, mul);
            }
            n = atoi(&entrada);
            mul[0][0] = (A[0][0]*As[n][0][0] + A[0][1]*As[n][1][0]) % 1000;
            mul[0][1] = (A[0][0]*As[n][0][1] + A[0][1]*As[n][1][1]) % 1000;
            mul[1][0] = (A[1][0]*As[n][0][0] + A[1][1]*As[n][1][0]) % 1000;
            mul[1][1] = (A[1][0]*As[n][0][1] + A[1][1]*As[n][1][1]) % 1000;
            copia(A, mul);
            scanf("%c", &entrada);
        }
        printf("%03d\n", A[0][1]);
        A[0][0] = 1; A[1][0] = 0; A[0][1] = 0; A[1][1] = 1;
    }

    return 0;
}



int ** multiplicao(int ** A, int ** B) {
    int ** aux = (int**)malloc(sizeof(int*)*2);
    aux[0] = (int*)malloc(sizeof(int)*2);
    aux[1] = (int*)malloc(sizeof(int)*2);
    aux[0][0] = A[0][0]*B[0][0] + A[0][1]*B[1][0];
    aux[0][1] = A[0][0]*B[0][1] + A[0][1]*B[1][1];
    aux[1][0] = A[1][0]*B[0][0] + A[1][1]*B[1][0];
    aux[1][1] = A[1][0]*B[0][1] + A[1][1]*B[1][1];
    return aux;
}

void copia(int ** A, int ** B) {
    int i, j;
    for (i = 0; i < 2; i++) {
        for (j = 0; j < 2; j++) {
            A[i][j] = B[i][j];
        }
    }
}
