/* FloidWarshall (Probabilidade) - C++ */
#include <iostream>
#include <sstream>
#include <string>
#include <stdlib.h>
#include <stdio.h>
#include <math.h>
#include <vector>

using namespace std;

int main() {
	vector < vector<double> > G;
	int N, M, i, j, k, x, y;
	double z;
	scanf("%d", &N);
	while (N != 0) {
		scanf("%d", &M);
		for (i = 0; i < N; i++) {
		    vector <double> row;
		    for (j = 0; j < N; j++) {
		    	row.push_back(0);
		   	}
		   	G.push_back(row);
		}
		for (i = 0; i < N; i++) {
			G[i][i] = 1;
		}
		for (i = 0; i < M; i++) {
			scanf("%d", &x);
			scanf("%d", &y);
			scanf("%lf", &z);
			G[x-1][y-1] = z/100;
			G[y-1][x-1] = z/100;
		}
		for (i = 0; i < N; i++) {
			for (j = 0; j < N; j++) {
				for (k = 0; k < N; k++) {
					if (G[i][k] < G[i][j] * G[j][k]) {
						G[i][k] = G[i][j] * G[j][k];
						G[k][i] = G[i][j] * G[j][k];
					}
				}
			}
		}
		printf("%.6f percent\n", G[0][N-1]*100);
		G.clear();
		scanf("%d", &N);
	}
    	return 0;
}
