#include <iostream>
#include <sstream>
#include <string>
#include <stdlib.h>
#include <stdio.h>

using namespace std;

int main()
{
    double cedula[] = {100, 50, 20, 10, 5, 2};
    double moeda[] = {100, 50, 25, 10, 5, 1};
    double valor;
    int i, k;

    cin >> valor;
    cout << "NOTAS:" << endl;
    for (i = 0; i < 6; i++) {
        k = valor/cedula[i];
        valor -= k*cedula[i];
        printf("%d nota(s) de R$ %.2f\n", (int) k, cedula[i]);
    }
    valor *=100;

    cout << "MOEDAS:" << endl;
    for (i = 0; i < 6; i++) {
        k = valor/moeda[i];
        valor -=  k*moeda[i];
        printf("%d moeda(s) de R$ %.2f\n", k, moeda[i]/100);
    }

    return 0;
}
