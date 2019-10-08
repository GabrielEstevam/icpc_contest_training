#include <iostream>
#include <sstream>
#include <string>
#include <stdlib.h>
#include <stdio.h>
#include <math.h>
#include <vector>

using namespace std;

int buscaLargura (vector < vector<int> > G);

int main() {
	int i, j, N, V, a, b;
	vector < vector<int> > G;
	cin >> N;
	cin >> V;
	for (i = 0; i < N; i++) {
		vector <int> row;
		for (j = 0; j < N; j++)
			row.push_back(0);		
		G.push_back(row);
	}
	for (i = 0; i < V; i++) {
		cin >> a;
		cin >> b;
		G[a - 1][b - 1] = 1;
		G[b - 1][a - 1] = 1;
	}
	cout << buscaLargura(G) << endl;
	G.clear();
    return 0;
}

int buscaLargura (vector < vector<int> > G) {
	int i, k, x;	
	int N = G.size();
	bool flagCor;
	vector <int> cor;
	for (i = 0; i < N; i++)
		cor.push_back(-1); //pinta de branco
	k = 0;
	while (true) {
		vector <int> fila;
		x = 0;
		while (cor[x] != -1)
			x += 1;
		fila.push_back(x);
		k += 1;
		while (fila.size() > 0) {
			x = fila[0];
			fila.erase(fila.begin()+0);
			cor[x] = k;
			for (i = 0; i < N; i++) {
				if (G[x][i] and cor[i] == -1) {
					cor[i] = 0;
					fila.push_back(i);
				}
			}
		}
		flagCor = true;
		for (i = 0; i < N; i++) {
			if (cor[i] == -1) {
				flagCor = false;
				break;
			}
		}
		if (flagCor)
			break;
		fila.clear();
	}
	cor.clear();
	return k;
}
