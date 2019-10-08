#include <iostream>
#include <sstream>
#include <string>
#include <stdlib.h>
#include <stdio.h>

using namespace std;

long long fatorial (int a);

int main()
{
    int a, b;

    while (cin >> a) {
        cin >> b;
        cout << fatorial(a) + fatorial(b) << endl;
    }

    return 0;
}

long long fatorial (int a) {
    long long fat = 1;
    int i;
    for (i = 2; i <= a; i++)
        fat *= i;
    return fat;
}
