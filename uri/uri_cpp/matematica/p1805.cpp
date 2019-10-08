#include <iostream>
#include <sstream>
#include <string>
#include <stdlib.h>
#include <stdio.h>

using namespace std;

int main()
{
    long long a, b, soma;

    cin >> a;
    cin >> b;

    soma = ((a+b)*(b-a+1))/2;

    cout << soma << endl;

    return 0;
}
