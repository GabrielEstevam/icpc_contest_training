#include <iostream>
#include <sstream>
#include <string>
#include <stdlib.h>
#include <stdio.h>
#include <math.h>
#include <vector>
#include <bits/stdc++.h>
#include <algorithm>

using namespace std;

int main() {
	int N, M, T, t, m, pivo, cont, entry, max = 0, imax = 0;
	cin >> T;
	for (t = 0; t < T; t++) {
		cin >> N;
		cin >> M;
		vector <int> v;
		for (m = 0; m < M; m++) {
			cin >> entry;
			v.push_back(entry);
		}
		sort(v.begin(), v.end());
		pivo = v[0];
		cont = 0;
		max = 0;
		imax = 0;
		for (m = 0; m < M; m++) {
			if (v[m] != pivo) {
				if (cont > max) {
					max = cont;
					imax = pivo;
				}
				cont = 0;
				pivo = v[m];
			}
			cont++;
		}
		
		if (cont > max) {
			max = cont;
			imax = pivo;
		}
		if (max*2 > M) {
			cout << imax << endl;
		} else {
			cout << "-1" << endl;
		}
	}
	return 0;
}
