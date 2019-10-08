#include <iostream>
#include <sstream>
#include <string>
#include <stdlib.h>
#include <stdio.h>
#include <math.h>
#include <algorithm>
#include <vector>

using namespace std;

int main() {
    int i, aux, k, entry;
    vector <bool> primos;
    vector <int> fat;
    vector <int> M;
    int N = 2*1000000+1;

    for (i = 0; i < N; i++) {
        primos.push_back(1);
        fat.push_back(2);
    }
    for (i = 2; i < N; i++) {
        if (primos[i]) {
            aux = i;
            k = 2;
            while (aux*k < N) {
                primos[aux*k] = 0;
                k += 1;
            }
        }
    }
    for (i = 2; i < N/2; i++) {
        aux = 2;
        while (aux * i < N) {
            fat[aux*i]++;
            aux++;
        }
    }
    /*for (i = 0; i < N; i++) {
        cout << i << ": " << fat[i] << endl;
    }*/

    M.push_back(0);
    M.push_back(0);
    for (i = 2; i < N; i++) {
        if (primos[fat[i]]) {
            M.push_back(M[i-1]+1);
        } else {
            M.push_back(M[i-1]);
        }
    }

    while (scanf("%d", &entry) != EOF) {
        printf("%d\n", M[entry]);
    }

    return 0;
}
