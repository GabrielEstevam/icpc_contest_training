#include <iostream>
#include <sstream>
#include <string>
#include <stdlib.h>
#include <stdio.h>
#include <math.h>

using namespace std;

int euclides(int a, int b);

int main()
{
    int instancias, a, b, i, j;

    cin >> instancias;
    for (i = 0; i < instancias; i++) {
        cin >> a;
        cin >> b;
        cout << euclides(a, b) << endl;
    }

    return 0;
}

int euclides(int a, int b) {
    if (b == 0) {
        return a;
    } else {
        return euclides(b, a%b);
    }
}
