#include <iostream>
#include <sstream>
#include <string>
#include <stdlib.h>
#include <stdio.h>
#include <math.h>

using namespace std;

int ** multiplicao(int ** A, int ** B);
void copia(int ** A, int ** B);
int stringToInteger(string a, int position);
void printMatriz(int ** A);

int main()
{
    long long i;
    int module, n;
    int caseValue = 1, j, k, a, b;
    string input = "";
    cin >> input;
    cin >> module;

    int *** As;
    int ** A, ** aux, ** mul;

    /* Pre calculo */
    As = (int***)malloc(sizeof(int**)*10);
    As[0] = (int**)malloc(sizeof(int*)*3);
    As[0][0] = (int*)malloc(sizeof(int)*3);
    As[0][1] = (int*)malloc(sizeof(int)*3);
    As[0][2] = (int*)malloc(sizeof(int)*3);
    As[0][0][0] = 1; As[0][0][1] = 0; As[0][0][2] = 0;
    As[0][1][0] = 0; As[0][1][1] = 1; As[0][1][2] = 0;
    As[0][2][0] = 0; As[0][2][1] = 0; As[0][2][2] = 1;

    As[1] = (int**)malloc(sizeof(int*)*3);
    As[1][0] = (int*)malloc(sizeof(int)*3);
    As[1][1] = (int*)malloc(sizeof(int)*3);
    As[1][2] = (int*)malloc(sizeof(int)*3);
    As[1][0][0] = 0; As[1][0][1] = 1; As[1][0][2] = 0;
    As[1][1][0] = 1; As[1][1][1] = 1; As[1][1][2] = 1;
    As[1][2][0] = 0; As[1][2][1] = 0; As[1][2][2] = 1;

    for (i = 2; i <= 9; i++)
        As[i] = multiplicao(As[i-1], As[1]);

    /* Fim do pre calculo */

    A = (int**)malloc(sizeof(int*)*3);
    A[0] = (int*)malloc(sizeof(int)*3);
    A[1] = (int*)malloc(sizeof(int)*3);
    A[2] = (int*)malloc(sizeof(int)*3);
    A[0][0] = 1; A[0][1] = 0; A[0][2] = 0;
    A[1][0] = 0; A[1][1] = 1; A[1][2] = 0;
    A[2][0] = 0; A[2][1] = 0; A[2][2] = 1;

    aux = (int**)malloc(sizeof(int*)*3);
    aux[0] = (int*)malloc(sizeof(int)*3);
    aux[1] = (int*)malloc(sizeof(int)*3);
    aux[2] = (int*)malloc(sizeof(int)*3);

    mul = (int**)malloc(sizeof(int*)*3);
    mul[0] = (int*)malloc(sizeof(int)*3);
    mul[1] = (int*)malloc(sizeof(int)*3);
    mul[2] = (int*)malloc(sizeof(int)*3);

    while (input.size() > 1 || stringToInteger(input, 0) != 0 || module != 0) {
        for (i = 0; i < input.size(); i++) {
            copia(aux, A);
            for (j = 0; j < 9; j++) {
                for (a = 0; a < 3; a++) {
                    for (b = 0; b < 3; b++) {
                        mul[a][b] = 0;
                        for (k = 0; k < 3; k++) {
                            mul[a][b] += (A[a][k] * aux[k][b]) % module;
                        }
                    }
                }
                copia(A, mul);
            }
            n = stringToInteger(input, i);
            for (a = 0; a < 3; a++) {
                for (b = 0; b < 3; b++) {
                    mul[a][b] = 0;
                    for (k = 0; k < 3; k++) {
                        mul[a][b] += (A[a][k] * As[n][k][b]) % module;
                    }
                }
            }
            copia(A, mul);
        }
        cout << "Case " << caseValue++ << ": " << input << " " << module << " " << ((A[0][0]+A[0][1]+A[0][2]) % module) << endl;
        A[0][0] = 1; A[0][1] = 0; A[0][2] = 0;
        A[1][0] = 0; A[1][1] = 1; A[1][2] = 0;
        A[2][0] = 0; A[2][1] = 0; A[2][2] = 1;
        cin >> input;
        cin >> module;
    }
    return 0;
}

int ** multiplicao(int ** A, int ** B) {
    int ** aux = (int**)malloc(sizeof(int*)*3);
    aux[0] = (int*)malloc(sizeof(int)*3);
    aux[1] = (int*)malloc(sizeof(int)*3);
    aux[2] = (int*)malloc(sizeof(int)*3);
    int i, j, k;
    for (i = 0; i < 3; i++) {
        for (j = 0; j < 3; j++) {
            aux[i][j] = 0;
            for (k = 0; k < 3; k++) {
                aux[i][j] += A[k][j] * B[i][k];
            }
        }
    }
    return aux;
}

void copia(int ** A, int ** B) {
    int i, j;
    for (i = 0; i < 3; i++) {
        for (j = 0; j < 3; j++) {
            A[i][j] = B[i][j];
        }
    }
}

int stringToInteger(string a, int position) {
    switch (a[position]) {
    case '0': return 0; break;
    case '1': return 1; break;
    case '2': return 2; break;
    case '3': return 3; break;
    case '4': return 4; break;
    case '5': return 5; break;
    case '6': return 6; break;
    case '7': return 7; break;
    case '8': return 8; break;
    case '9': return 9; break;
    }
    return 0;
}

void printMatriz(int ** A) {
    int i, j;
    for (i = 0; i < 3; i++) {
        for (j = 0; j < 3; j++) {
            cout << "|" << A[i][j] << "|";
        }
        cout << endl;
    }
    cout << endl;
}
