#include <iostream>
#include <sstream>
#include <string>
#include <stdlib.h>
#include <stdio.h>
#include <math.h>
#include <vector>
#include <set>

using namespace std;

int main() {
    int N, M, I, i, j, k, entry, x, y, aux, menor;
    string entrys;
    vector <int> idade;
    vector <int> pos;
    vector < vector <int> > gerente;
    set <int> fila;
    
    while (cin >> N) {
        cin >> M;
        cin >> I;

        for (i = 0; i < N; i++) {
            cin >> entry;
            idade.push_back(entry);
            pos.push_back(i);
        }
        for (i = 0; i < N; i++) {
            vector <int> row;
            gerente.push_back(row);
        }
        for (i = 0; i < M; i++) {
            cin >> x;
            cin >> y;
            gerente[y-1].push_back(x-1);
        }
        for (i = 0; i < I; i++) {
            cin >> entrys;
            if (entrys == "T") {
                cin >> x;
                x -= 1;
                cin >> y;
                y -= 1;
                aux = idade[pos[x]];
                idade[pos[x]] = idade[pos[y]];
                idade[pos[y]] = aux;
                aux = pos[x];
                pos[x] = pos[y];
                pos[y] = aux;
            } else {
                cin >> entry;
                menor = -1;
                for (j = 0; j < gerente[pos[entry-1]].size(); j++) {
                    fila.insert(gerente[pos[entry-1]][j]);
                }
                while (fila.size() > 0) {
                    k = *(fila.begin());
                    fila.erase(fila.begin());
                    if (idade[k] < menor or menor == -1) {
                        menor = idade[k];
                    }
                    for (j = 0; j < gerente[k].size(); j++) {
                        fila.insert(gerente[k][j]);
                    }
                    
                }
                if (menor == -1) {
                    cout << "*" << endl;
                } else {
                    cout << menor << endl;
                }
            }
        }
        fila.clear();
        idade.clear();
        pos.clear();
        gerente.clear();
        
    }
    
    return 0;
}
