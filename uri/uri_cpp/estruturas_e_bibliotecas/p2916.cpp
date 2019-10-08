#include <iostream>
#include <sstream>
#include <string>
#include <stdlib.h>
#include <stdio.h>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    long long N, K, entry, i, soma;
    vector <long long> v;

    while (cin >> N) {
        cin >> K;
        for (i = 0; i < N; i++) {
            scanf("%ld", &entry);
            v.push_back(entry);
        }
        sort(v.begin(), v.end());
        soma = 0;
        for (i = N-1; i > (N-K-1); i--)
            soma += v[i];
        printf("%ld\n", (soma % 1000000007));
        v.clear();
    }

    return 0;
}