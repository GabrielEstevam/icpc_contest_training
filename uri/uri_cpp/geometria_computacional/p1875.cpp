#include <iostream>
#include <sstream>
#include <string>
#include <stdlib.h>
#include <stdio.h>
#include <math.h>

using namespace std;

int main()
{
    int instancias, entradas, i, j;
    char a, b;
    int RGB[] = {0,0,0};

    cin >> instancias;
    for (i = 0; i < instancias; i++) {
        cin >> entradas;
        for (j = 0; j < entradas; j++) {
            cin >> a;
            cin >> b;
            if (a == 'R') {
                if (b == 'G')
                    RGB[0] += 2;
                else
                    RGB[0]++;
            } else if (a == 'G') {
                if (b == 'B')
                    RGB[1] += 2;
                else
                    RGB[1]++;
            } else if (a == 'B') {
                if (b == 'R')
                    RGB[2] += 2;
                else
                    RGB[2]++;
            }
        }
        if (RGB[0] == RGB[1] && RGB[0] == RGB[2]) {
            cout << "trempate" << endl;
        } else if (RGB[0] > RGB[1] && RGB[0] > RGB[2]) {
            cout << "red" << endl;
        } else if (RGB[1] > RGB[0] && RGB[1] > RGB[2]) {
            cout << "green" << endl;
        } else if (RGB[2] > RGB[0] && RGB[2] > RGB[1]) {
            cout << "blue" << endl;
        } else {
            cout << "empate" << endl;
        }
        RGB[0] = 0; RGB[1] = 0; RGB[2] = 0;
    }

    return 0;
}
