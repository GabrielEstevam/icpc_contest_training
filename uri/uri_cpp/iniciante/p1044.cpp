#include <iostream>
#include <sstream>
#include <string>
#include <stdlib.h>
#include <stdio.h>

using namespace std;

int main()
{
    int a, b;

    cin >> a;
    cin >> b;

    if (a != 0 && b != 0) {
        if (a < b) {
            if (b % a == 0) {
                cout << "Sao Multiplos" << endl;
            } else {
                cout << "Nao sao Multiplos" << endl;
            }
        } else {
            if (a % b == 0) {
                cout << "Sao Multiplos" << endl;
            } else {
                cout << "Nao sao Multiplos" << endl;
            }
        }
    } else {
        cout << "Nao sao Multiplos" << endl;
    }

    return 0;
}
