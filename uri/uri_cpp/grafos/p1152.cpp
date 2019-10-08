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

int main() {
	vector < vector<int> > m;
	vector <int> pai;
	int N, M, i, paix, paiy, x, y, z, cont, soma;
	
	scanf("%d", &N);
	scanf("%d", &M);
	while (N != 0) {
		for (i = 0; i < M; i++) {
			vector <int> row;
			scanf("%d", &x);
			scanf("%d", &y);
			scanf("%d", &z);
			row.push_back(z);
			row.push_back(x);
			row.push_back(y);
			row.push_back(0);
		   	m.push_back(row);
		}
		for (i = 0; i < N; i++) {
			pai.push_back(i);
		}
		sort(m.begin(), m.end());
		cont = 0;
		i = 0;
		while (cont < N - 1) {
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
		soma = 0;
		for (i = 0; i < M; i++) {
			soma += m[i][0] * (1 - m[i][3]);
		}
		printf("%d\n", soma);
		m.clear();
		pai.clear();
		scanf("%d", &N);
		scanf("%d", &M);
	}
    	return 0;
}
