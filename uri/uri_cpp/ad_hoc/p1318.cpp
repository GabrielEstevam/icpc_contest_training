#include <iostream>
#include <sstream>
#include <string>
#include <stdlib.h>
#include <stdio.h>
#include <math.h>
#include <vector>

using namespace std;

int main() {
	int N, M, i, entry, count;
	vector <int> bilhetes;

	while (true) {
		cin >> N;		
		cin >> M;
		if (N == 0 and M ==0)
			break;
		for (i = 0; i < N; i++)
			bilhetes.push_back(0);
		for (i = 0; i < M; i++) {
			cin >> entry;
			bilhetes[entry-1]++;
		}
		count = 0;
		for (i = 0; i < N; i++) {
			if (bilhetes[i] > 1)
				count++;
		}
		cout << count << endl;
		bilhetes.clear();
	}

    return 0;
}
