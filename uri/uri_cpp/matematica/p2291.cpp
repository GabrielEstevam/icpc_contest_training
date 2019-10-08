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
	vector <int> soma;
	vector <long long> divino;
	N = 1000000;
	soma.push_back(0);
	for (i = 1; i <= N; i++) {
		soma.push_back(0);
	}	
	for (i = 1; i <= N; i++) {
		j = 1;
		while (i*j <= N) {
			soma[i*j] += i;
			j++;		
		}
	}
	divino.push_back(0);
	for (i = 1; i <= N; i++) {
		divino.push_back(divino[i-1]+soma[i]);
	}
	
	/*for (i = 1; i <= N; i++) {
		cout << divino[i] << " ";
	}
	cout << endl;*/
	cin >> entry;
	while (entry != 0) {
		cout << divino[entry] << endl;
		cin >> entry;
	}
    return 0;
}

