#include <iostream>
#include <sstream>
#include <string>
#include <stdlib.h>
#include <stdio.h>
#include <math.h>

using namespace std;

int fibonacci (int k);
static int calls = 0;

int main()
{
    int instancias, i, entrada;
    cin >> instancias;
    for (i = 0; i < instancias; i++) {
        cin >> entrada;
        cout << "fib(" << entrada << ") = " << (calls-1) << " calls = " << fibonacci(entrada) << endl;
        calls = 0;
    }
    return 0;
}

int fibonacci (int k) {
    calls++;
    if (k == 0) {
        return 0;
    } else if (k == 1) {
        return 1;
    } else {
        return fibonacci(k-1)+fibonacci(k-2);
    }
}
