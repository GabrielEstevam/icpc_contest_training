#include <iostream>
#include <sstream>
#include <string>
#include <stdlib.h>
#include <stdio.h>
#include <algorithm>
#include <vector>

using namespace std;

int main() {
    int N, i, x, y, z, w;
    vector < vector <double> > v;
    scanf("%d", &N);
    while (N > 0) {
        for (i = 0; i < N; i++) {
            vector <double> row;
            row.push_back(0);
            row.push_back(0);
            row.push_back(double(i+1));
            row.push_back(0);
            v.push_back(row);
        }
        for (i = 0; i < int((N*(N-1))/2); i++) {
            scanf("%d", &x);
            scanf("%d", &y);
            scanf("%d", &z);
            scanf("%d", &w);
            v[x-1][0]++;
            v[z-1][0]++;
            if (y > w)
                v[x-1][0]++;
            else
                v[z-1][0]++;
            v[x-1][1] += y;
            v[x-1][3] += w;
            v[z-1][1] += w;
            v[z-1][3] += y;
        }
        for (i = 0; i < N; i++) {
            if (v[i][3] != 0)
                v[i][1] /= v[i][3];
            else
                v[i][1] /= (N-1);
        }
        sort(v.begin(), v.end());
        for (i = 0; i < N; i++) {
            for (int j = 0; j < 4; j++)
                printf("%f ", v[i][j]);
            printf("\n");
        }
        printf("\n");
        scanf("%d", &N);
    }
    return 0;
}
