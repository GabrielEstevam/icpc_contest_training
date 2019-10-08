#include <iostream>
#include <sstream>
#include <string>
#include <stdlib.h>
#include <stdio.h>

using namespace std;

int main()
{
    char nome[100];
    double entrada;
    double distancia = 0;
    int quantidade = 0;

    while (gets(nome)) {
        scanf("%lf%*c", &entrada);
        distancia += entrada;
        quantidade++;
    }
    printf("%.1f\n", (distancia/quantidade));
    return 0;
}
