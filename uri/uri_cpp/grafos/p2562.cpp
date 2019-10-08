#include <iostream>
#include <sstream>
#include <string>
#include <stdlib.h>
#include <stdio.h>
#include <math.h>
#include <vector>

using namespace std;

int main() {
    int V, A, E, i, x, y, cont, topo;
    vector < vector <int> > G;
    vector <int> cor;
    vector <int> pilha;

    while (cin >> V) {
        cin >> A;

        for (i = 0; i < V; i++) {
            vector <int> row;
            G.push_back(row);
            cor.push_back(1);
        }
        for (i = 0; i < A; i++) {
            cin >> x;
            cin >> y;
            G[x-1].push_back(y-1);
            G[y-1].push_back(x-1);
        }
        cin >> E;
        E -= 1;
        pilha.push_back(E);
        cor[E] = 0;
        cont = 1;
        while (pilha.size() > 0) {
            topo = pilha.back();
            pilha.pop_back();
            for (i = 0; i < G[topo].size(); i++) {
                if (cor[G[topo][i]]) {
                    pilha.push_back(G[topo][i]);
                    cor[G[topo][i]] = 0;
                    cont += 1;
                }
            }
        }
        cout << cont << endl;
        G.clear();
        cor.clear();
        pilha.clear();
        cont = 0;
    }

    return 0;
}
