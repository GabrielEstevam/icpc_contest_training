#include <iostream>
#include <sstream>
#include <string>
#include <stdlib.h>
#include <stdio.h>

using namespace std;

int main()
{
    float x, y;

    cin >> x;
    cin >> y;

    if (x == 0 && y == 0)
        cout << "Origem" << endl;
    else if (y == 0)
        cout << "Eixo X" << endl;
    else if (x == 0)
        cout << "Eixo Y" << endl;
    else if (x > 0 && y > 0)
        cout << "Q1" << endl;
    else if (x > 0 && y < 0)
        cout << "Q4" << endl;
    else if (x < 0 && y > 0)
        cout << "Q2" << endl;
    else if (x < 0 && y < 0)
        cout << "Q3" << endl;

    return 0;
}
