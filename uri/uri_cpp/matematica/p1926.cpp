#include <iostream>
#include <sstream>
#include <string>
#include <stdlib.h>
#include <stdio.h>
#include <math.h>
#include <vector>

using namespace std;

int main() {
    int i, j, k = 0, N = 1000003, Q, x, y;
    vector <bool> v;
    vector <int> twin;
    for (i = 0; i < N; i++)
        v.push_back(1);
    v[0] = 0;
    v[1] = 0;
    for (i = 2; i < N; i++) {
        if (v[i]) {
            for (j = i+i; j < N; j += i)
                v[j] = 0;
        }
    }
    twin.push_back(0);
    twin.push_back(0);
    for (i = 2; i < N-2; i++) {
        if (v[i] and (v[i-2] or v[i+2]))
            k += 1;
        twin.push_back(k);
    }
    scanf("%d", &Q);
    for (i = 0; i < Q; i++) {
        scanf("%d", &x);
        scanf("%d", &y);
        printf("%d\n", abs(twin[y]-twin[x-1]));
    }
    return 0;
}
