#include <iostream>
#include <sstream>
#include <string>
#include <stdlib.h>
#include <stdio.h>
#include <math.h>
#include <algorithm>

using namespace std;


int main()
{
    int instancias, N, M;
    int C;
    int * input;
    int i, j;
    int energy = 0, travels = 0;

    cin >> instancias;
    for (i = 0; i < instancias; i++) {
        cin >> N;
        cin >> C;
        cin >> M;
        input = (int*)malloc(sizeof(int)*M);
        for (j = 0; j < M; j++)
            cin >> input[j];
        sort(input, input+M);
        travels = ceil(M/(double)C);
        for (j = 0; j < travels; j++)
            energy += 2*input[M-1-C*j];
        cout << energy << endl;
        energy = 0;
    }

    return 0;
}
