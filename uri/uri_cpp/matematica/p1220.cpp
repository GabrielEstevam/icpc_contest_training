#include <iostream>
#include <sstream>
#include <string>
#include <stdlib.h>
#include <stdio.h>
#include <math.h>

using namespace std;

int main()
{
    int instancias;
    int i;
    double in;
    int * entrada;
    int total, media, resultado, upper, lower, uk, lk;

    cin >> instancias;

    double * result = (double*)malloc(sizeof(double)*100);
    int k = 0;

    while (instancias != 0) {
        total = 0;
        entrada = (int*)malloc(sizeof(int)*instancias);
        for (i = 0; i < instancias; i++) {
            cin >> in;
            entrada[i] = (round(in*100));
            total += entrada[i];
        }
        media = round((double)total/instancias);
        upper = 0;
        lower = 0;
        uk = 0;
        lk = 0;
        resultado = 0;
        for (i = 0; i < instancias; i++) {
            if (entrada[i] > media) {
                upper += entrada[i] - media;
                uk++;
            } else if (entrada[i] < media){
                lower += media - entrada[i];
                lk++;
            }
        }
        resultado = (lower <= upper) ? lower : upper;
        if (lk != 0)
            resultado += floor((double) floor((double) abs(lower-upper)/2)/lk);
        printf("$%.2f\n", (double) resultado/100);
        result[k++] = resultado;
        free(entrada);
        cin >> instancias;
    }
    for (i = 0; i < k; i++)
        //printf("$%.2f\n", (double) result[i]/100);

    return 0;
}
