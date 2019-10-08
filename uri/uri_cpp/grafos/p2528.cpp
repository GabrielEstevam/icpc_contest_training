#include <iostream>
#include <sstream>
#include <string>
#include <stdlib.h>
#include <stdio.h>
#include <math.h>
#include <vector>

using namespace std;

vector < vector<long> > dijkstra (vector < vector <int> > G);

int main() {
    int N, V, x, y, i, j;
    vector < vector <int> > G;
    vector < vector <long> > retorno;
    int C, R, E;

    while (cin >> N) {
        scanf("%d", &V);
        for (i = 0; i < N+1; i++) {
            vector <int> row;
            for (j = 0; j < N+1; j++) {
                row.push_back(0);
            }
            G.push_back(row);
        }
        for (i = 0; i < V; i++) {
            scanf("%d", &x);
            scanf("%d", &y);
            G[x][y] = 1;
            G[y][x] = 1;
        }
        scanf("%d", &C);
        scanf("%d", &R);
        scanf("%d", &E);
        G[0][C] = 1;
        G[C][0] = 1;
        for (i = 0; i < N+1; i++) {
            G[E][i] = 0;
            G[i][E] = 0;
        }
        retorno = dijkstra(G);
        printf("%d\n", retorno[1][R]-1);
        G.clear();
        retorno.clear();
    }

    return 0;
}

vector < vector<long> > dijkstra (vector < vector <int> > G) {
    int N = G.size();
    int i, u, v, lenFila;
    vector <long> D;
    vector <bool> Flag;
    for (i = 0; i < N; i++) {
        D.push_back(100000000); //atribui infinito
        Flag.push_back(true);
    }
    D[0] = 0;
    lenFila = N;
    vector <long> arvore;
    for (i = 0; i < N; i++) {
        arvore.push_back(-1);
    }
    while (lenFila > 0) {
        u = 0;
        while (Flag[u] == false) {
            u += 1;
        }
        for (i = 0; i < N; i++) {
            if (Flag[i] and D[i] < D[u]) {
                u = i;
            }
        }
        Flag[u] = 0;
        lenFila -= 1;
        for (v = 0; v < N; v++) {
            if (G[u][v] > 0 and D[v] > D[u] + G[u][v]) {
                D[v] = D[u] + G[u][v];
                arvore[v] = u;
            }
        }
    }
    vector < vector <long> > retorno;
    retorno.push_back(arvore);
    retorno.push_back(D);
    return retorno;
}