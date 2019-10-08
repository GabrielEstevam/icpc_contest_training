#include <iostream>
#include <sstream>
#include <string>
#include <stdlib.h>
#include <stdio.h>

using namespace std;

int main()
{
    int instancias;
    char entrada;
    int i, k;
    int led[] = {6,2,5,5,4,5,6,3,7,6};
    int leds = 0;

    cin >> instancias;
    cin.ignore();
    for (i = 0; i < instancias; i++) {
        entrada = getc(stdin);
        while (isdigit(entrada)) {
            k = atoi(&entrada);
            leds += led[k];
            entrada = getc(stdin);
        }
        cout << leds << " leds" << endl;
        leds = 0;
    }

    return 0;
}
