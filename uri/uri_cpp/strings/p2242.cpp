#include <iostream>
#include <sstream>
#include <string>
#include <stdlib.h>
#include <stdio.h>

using namespace std;

bool vogal (char c);

int main()
{
    string entrada;
    char vogais[50];
    int i, topo = 0;

    cin >> entrada;
    for (i = 0; i < entrada.size(); i++) {
        if (vogal(entrada[i]))
            vogais[topo++] = entrada[i];
    }

    for (i = 0; i < topo/2; i++) {
        if (vogais[i] != vogais[topo-i-1]) {
            cout << "N" << endl;
            return 0;
        }
    }
    cout << "S" << endl;

    return 0;
}

bool vogal (char c) {
    switch (c) {
        case 'a':
            return true;
        case 'e':
            return true;
        case 'i':
            return true;
        case 'o':
            return true;
        case 'u':
            return true;
        default:
            return false;
    }
}
