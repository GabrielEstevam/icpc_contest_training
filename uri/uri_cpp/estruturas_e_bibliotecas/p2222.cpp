#include <iostream>
#include <sstream>
#include <string>
#include <stdlib.h>
#include <stdio.h>
#include <math.h>
#include <vector>
#include <algorithm>
#include <set>
#include <utility>
#include <bitset>

using namespace std;

int main() {
	int T, t, N, n, M, Q, q, a, b, i, entry;
	vector < vector <int> > C;
	set <int>::iterator it;
	pair < set<int>::iterator, bool> ret;
	cin >> T;
	for (t = 0; t < T; t++) {
		cin >> N;
		for (n = 0; n < N; n++) {
			cin >> M;
			vector <int> row;
			for (i = 0; i < M; i++) {
				cin >> entry;
				row.push_back(entry);
			}
			C.push_back(row);
		}
		
		cin >> Q;
		for (n = 0; n < Q; n++) {
			cin >> q;
			cin >> a;
			a -= 1;
			cin >> b;
			b -= 1;
			if (q == 2) {
				set <int> Uniao;
				bitset<7> byte;
				for (i = 0; i < C[a].size(); i++) {
					Uniao.insert(C[a][i]);
				}
				for (i = 0; i < C[b].size(); i++) {
					Uniao.insert(C[b][i]);
				}
				cout << Uniao.size() << endl;
				Uniao.clear();	
			}else {
				set <int> Intersecao;
				int cont = 0;
				for (i = 0; i < C[a].size(); i++) {
					Intersecao.insert(C[a][i]);
				}
				for (i = 0; i < C[b].size(); i++) {
					ret = Intersecao.insert(C[b][i]);
					if (ret.second == false)
						cont += 1;
				}
				cout << cont << endl;
				Intersecao.clear();
			}
		}
		C.clear();
	}

    return 0;
}
