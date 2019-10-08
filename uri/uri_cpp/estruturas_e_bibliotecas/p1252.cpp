#include <iostream>
#include <sstream>
#include <string>
#include <stdlib.h>
#include <stdio.h>
#include <math.h>
#include <vector>
#include <bits/stdc++.h>

using namespace std;

bool func(const pair<int, int> &a, const pair<int, int> &b) {
	if (a.second < b.second) {
		return (a.second < b.second);
	} else if (a.second == b.second) {
		if (a.first % 2 != 0 and b.first % 2 == 0) {
			return (a.second <= b.second);
		} else if (a.first % 2 != 0 and b.first % 2 != 0) { 
			return (a.first > b.first);		
		} else if (a.first % 2 == 0 and b.first % 2 == 0) {
			return (a.first < b.first);
		} else {
			return (a.second < b.second);
		}
	} else {
		return (a.second < b.second);
	}
}

int main() {
	int N, M, i, entry;
	vector< pair <int, int> > numeros;

	cin >> N;
	cin >> M;
	while (N > 0) {
		for (i = 0; i < N; i++) {
			cin >> entry;	
			numeros.push_back(make_pair(entry, entry % M));	
		}
		
		sort(numeros.begin(), numeros.end(), func);
		
		cout << N << " " << M << endl;
		for (i = 0; i < N; i++) {
			cout << numeros[i].first << endl;
		}		

		numeros.clear();
		cin >> N;
		cin >> M;
	}
	cout << "0 0" << endl;

	return 0;
}


