#include <iostream>
#include <sstream>
#include <string>
#include <stdlib.h>
#include <stdio.h>
#include <math.h>
#include <vector>

using namespace std;

vector<int> dijkstra (vector < vector<int> > G, int v);

int main() {
	/*vector <int> lista;
	lista.push_back(1);
	lista.push_back(2);
	lista.insert(lista.begin()+2, 1, 3);
	for (int i = 0; i < lista.size(); i++) {
		cout << lista[i] << " ";
	}
	cout << endl;*/
	vector < vector<int> > grafo;
	vector < vector<int> > buscas;
	vector <int> D;
	int N, V, i, j, k, v, x, y, h, d = 0;
	cin >> N;
	cin >> V;
	while (N != 0 or V != 0) {
		for (i = 0; i < N; i++) {
			vector <int> row;
			grafo.push_back(row);
			for (j = 0; j < N; j++) {
				grafo[i].push_back(-1);
			}
			vector <int> rows;
			buscas.push_back(rows);
		}
		for (v = 0; v < V; v++) {
			cin >> x;
			cin >> y;
			cin >> h;
			if (grafo[y-1][x-1] > -1) {
				grafo[y-1][x-1] = 0;
				grafo[x-1][y-1] = 0;
			} else {
				grafo[x-1][y-1] = h;
			}
		}
		cin >> k;
		for (i = 0; i < k; i++) {
			cin >> x;
			cin >> y;
			if (buscas[x-1].size() > 0) {
				D = buscas[x-1];
			} else {
				D = dijkstra(grafo, x-1);
				buscas[x-1] = D;
			}
			if (D[y-1] == 1000000000) {
				cout << "Nao e possivel entregar a carta" << endl;
			} else {
				cout << D[y-1] << endl;
			}
		}
		cout << endl;
		cin >> N;
		cin >> V;
		grafo.clear();
		buscas.clear();
		D.clear();
	}
    	return 0;
}

vector<int> dijkstra (vector< vector<int> > G, int v) {
	int N = G.size();
	vector <int> D;
	vector <bool> cor;
	vector <int> fila;
	int i, j, u;
	for (i = 0; i < N; i++) {
		D.push_back(1000000000);
		cor.push_back(true);
	}
	D[v] = 0;
	cor[v] = 0;
	fila.push_back(v);
	while (fila.size() > 0) {
		/*cout << "f: ";		
		for (i = 0; i < fila.size(); i++) {
			cout << fila[i] << " ";
		}
		cout << endl;*/
		u = fila[0];
		fila.erase(fila.begin());
		for (i = 0; i < N; i++) {
			if (G[u][i] > -1) {
				if (D[i] > D[u] + G[u][i]) {
					D[i] = D[u] + G[u][i];
					if (cor[i]) {
						for (j = 0; j < fila.size(); j++) {
							if (D[i] <= D[fila[j]])
								break;
						}
						fila.insert(fila.begin()+j, 1, i);
						cor[i] = 0;
					}
				}
			}
		}
		/*if (fila.size() == 1) {
			for (i = 0; i < N; i++) {
				if (cor[i]) {
					fila.push_back(i);
					cor[i] = 0;
					break;
				}
			}
		}*/
		/*cout << "d: ";
		for (i = 0; i < N; i++) {
			cout << D[i] << " ";
		}
		cout << endl;*/
	}
	return D;
}
