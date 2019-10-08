#include <iostream>
#include <sstream>
#include <string>
#include <stdlib.h>
#include <stdio.h>
#include <math.h>

using namespace std;

int main()
{
    int horario_anterior = 0, velocidade = 0, distancia = 0;
    int h, v, d;
    string entry, entry_anterior;
    bool flag1 = false, flag2 = false;
    while (cin >> entry) {
        if (entry.size() == 8) {
            h = int(entry[0] * 10 * 3600) + int(entry[1] * 3600);
            h += int(entry[3] * 10 * 360) + int(entry[4] * 360);
            h += int(entry[6] * 10) + int(entry[7]);
            if (flag1)
                flag2 = true;
            else
                flag1 = true;
        } else {
            v = atoi(entry.c_str());
            distancia += ((h - horario_anterior) * velocidade) / 3600;
            velocidade = v;
            horario_anterior = h;
            flag1 = false;
            flag2 = false;
        }
        if (flag1 && flag2) {
            d = distancia + ((h - horario_anterior) * velocidade) / 3600;
            cout << entry_anterior << " " << distancia << "km" << endl;
            flag1 = false;
            flag2 = false;
        }
        entry_anterior = entry;
    }


    return 0;
}
