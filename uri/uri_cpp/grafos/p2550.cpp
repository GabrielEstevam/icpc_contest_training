/* Kruskal (Arvore Geradora Minima) - C++*/

#include <iostream>
#include <sstream>
#include <string>
#include <stdlib.h>
#include <stdio.h>
#include <math.h>
#include <vector>
#include <algorithm>

using namespace std;

int find(vector<int> pai, int x);

int main() {
	vector < vector<int> > m;
	vector <int> pai;
	int N, M, i, j, paix, paiy, x, y, z, cont, soma, aux;
	bool flag;
	
	while (cin >> N) {
		scanf("%d", &M);
		for (i = 0; i < M; i++) {
			vector <int> row;
			scanf("%d", &x);
			scanf("%d", &y);
			scanf("%d", &z);
			row.push_back(z);
			row.push_back(x-1);
			row.push_back(y-1);
			row.push_back(0);
		   	m.push_back(row);
		}
		for (i = 0; i < N; i++) {
			pai.push_back(i);
		}
		sort(m.begin(), m.end());
		cont = 0;
		i = 0;
		while (cont < N - 1 and i < M) {
			paix = m[i][1];
			paix = pai[paix];
			while (paix != pai[paix]) {
				paix = pai[paix];	
			}
			paiy = m[i][2];
			paiy = pai[paiy];
			while (paiy != pai[paiy]) {
				paiy = pai[paiy];	
			}
			if (paix != paiy) {
				pai[paix] = paiy;
				cont += 1;
				m[i][3] = 1;
			}
			i++;	
		}
		
		flag = true;
		aux = find(pai, 0);
		for (i = 1; i < N; i++) {
			x = find(pai, i);
			if (x != aux) {
				flag = false;
				break;
			}
		}
		if (flag) {
			soma = 0;
			for (i = 0; i < M; i++) {
				soma += (m[i][0] * m[i][3]);
			}
			printf("%d\n", soma);
		} else {
			printf("impossivel\n");
		}
		m.clear();
		pai.clear();
	}
    	return 0;
}

int find(vector<int> pai, int x) {
	int aux;		
	if (pai[x] == x) {
		return x;
	} else {
		aux = x;
		while(pai[aux] != aux) {
			aux = pai[aux];
		}
		return aux;
	}
}
