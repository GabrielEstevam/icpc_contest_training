#include <iostream>
#include <sstream>
#include <string>
#include <stdlib.h>
#include <stdio.h>

using namespace std;

int main()
{
    int instancias;
    string entrada1, entrada2, saida = "";
    int k, i = 0, j = 0;

    cin >> instancias;
    for (k = 0; k < instancias; k++) {
        cin >> entrada1;
        cin >> entrada2;
        while (i < entrada1.size() && j < entrada2.size()) {
            if (j < i)
                saida += entrada2[j++];
            else
                saida += entrada1[i++];
        }
        while (i < entrada1.size())
            saida += entrada1[i++];
        while (j < entrada2.size())
            saida += entrada2[j++];
        cout << saida << endl;
        saida = "";
        i = 0;
        j = 0;
    }

    return 0;
}
