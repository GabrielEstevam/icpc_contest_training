#include <iostream>
#include <sstream>
#include <string>
#include <stdlib.h>
#include <stdio.h>
#include <vector>
#include <math.h>

using namespace std;

int main() {
	int N, i, j, k, entry;
	string entryS;
	vector < vector <int> > v;
	vector < string > name;
	scanf("%d", &N);

	while (N != 0) {
		for (i = 0; i < N; i++) {
			cin >> entryS;
			name.push_back(entryS);
			scanf("%d", &entry);
			vector <int> row;
			row.push_back(entry);
			row.push_back(i);
			v.push_back(row);
		}
		j = 0;
		k = v[0][0];
		if (k % 2 == 0)
			k = N-1;
		while (1) {
			if (k % 2 == 1) {
				j += k;
			} else {
				j -= (k - 1);
			}
			if (j < 0)
				j += N*ceil((float)abs(j)/N);
			j = j % N;
			k = v[j][0];
			v.erase(v.begin()+j);
			j -= 1;
			N -= 1;
			if (N == 1)
				break;
		}
		cout << "Vencedor(a): " << name[v[0][1]] << endl;
		v.clear();
		name.clear();
		scanf("%d", &N);
	}
    return 0;
}