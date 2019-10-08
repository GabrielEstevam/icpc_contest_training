#include <iostream>
#include <sstream>
#include <string>
#include <stdlib.h>
#include <stdio.h>
#include <math.h>
#include <vector>

using namespace std;

int main() {
	int N, i, j, entry;
	vector < vector <int> > G;
	vector <int> cor;
	bool flag = true;

	scanf("%d", &N);
	for (i = 0; i < N; i++) {
		vector <int> row;
		for (j = 0; j < N; j++) {
			scanf("%d", &entry);
			row.push_back(entry);
		}
		G.push_back(row);
	}
	for (i = 0; i < N; i++) {
		cor.push_back(0);
	}
	for (i = 0; i < N; i++) {
		for (j = 0; j < N; j++) {
			if (G[i][j] == 0) {
				cor[j] = 1 - cor[i];
			}
		}
	}

	for (i = 0; i < N; i++) {
		for (j = 0; j < N; j++) {
			if (cor[i] == cor[j] and G[i][j] == 0) {
				flag = false;
				break;
			}
		}
	}
	if (flag) {
		printf("Bazinga!\n");
	} else {
		printf("Fail!\n");
	}

    return 0;
}