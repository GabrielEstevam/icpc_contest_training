#include <iostream>
#include <sstream>
#include <string>
#include <stdlib.h>
#include <stdio.h>

using namespace std;

int maior (int a, int b);
int menor (int a, int b);

int main()
{
    int a, b, c;
    int d, e, f;

    cin >> a;
    cin >> b;
    cin >> c;

    d = menor(menor(a,b),menor(a,c));
    f = maior(maior(a,b),maior(a,c));
    e = a+b+c-d-f;

    cout << d << endl << e << endl << f << endl;
    cout << endl;
    cout << a << endl << b << endl << c << endl;

    return 0;
}

int maior (int a, int b) {
    if (a > b)
        return a;
    else
        return b;
}

int menor (int a, int b) {
    if (a < b)
        return a;
    else
        return b;
}
