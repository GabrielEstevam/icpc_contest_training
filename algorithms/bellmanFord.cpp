/* (Grafos) Bellman-Ford */
#include <iostream>
#include <sstream>
#include <string>
#include <stdlib.h>
#include <stdio.h>
#include <math.h>
#include <vector>

using namespace std;

int bellmanFord (vector < vector<int> > G, vector <int> C, int v, int x, int N);

int main() {
	int N, M, K, A;
	float P;
	vector < vector<int> > G;
	vector <int> C;
	int i, j, a, b, D;

	while (cin >> N) {
		cin >> M;
		cin >> K;
		cin >> P;
		for (i = 0; i < N; i++) {
			vector <int> row;
			for (j = 0; j < N; j++)
				row.push_back(0);
			G.push_back(row);
			C.push_back(0);
		}
		for (i = 0; i < M; i++) {
			cin >> a;
			cin >> b;
			G[a - 1][b - 1] = 1;
			G[b - 1][a - 1] = 1;
		}
		cin >> A;
		for (i = 0; i < A; i++) {
			cin >> a;
			C[a - 1] += 1;
		}
		cin >> a;
		cin >> b;
		D = bellmanFord (G, C, a - 1, b - 1, N);
		if (D <= K) {
			printf("%.3f\n", pow(P, D));
		} else {
			cout << "0.000" << endl;
		}
		G.clear();
		C.clear();
	}

    return 0;
}

int bellmanFord (vector < vector<int> > G, vector <int> C, int v, int x, int N) {
	int i, j, k;
	bool flag;
	vector <int> D;
	for (i = 0; i < N; i++)
		D.push_back(10000);
	D[v] = C[v];
	for (k = 0; k < N; k++) {
		flag = true;
		for (i = 0; i < N; i++) {
			for (j = 0; j < N; j++) {
				if (G[i][j]) {				
					if (D[j] > D[i] + C[j]) {
						D[j] = D[i] + C[j];
						flag = false;
					}		
				}
			}
		}
		if (flag)
			break;
	}
	return D[x];
}
