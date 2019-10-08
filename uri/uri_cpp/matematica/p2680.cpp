#include <iostream>
#include <sstream>
#include <string>
#include <stdlib.h>
#include <stdio.h>
#include <math.h>
#include <vector>

using namespace std;


int main() {
	int N, i, j, soma, entry;
	cin >> N;
	for (i = 0; i < N; i++) {
		cin >> entry;
		soma = 0;
		j = 1;
		while (j*j < entry) {
			if (entry % j == 0) {
				soma += j;
				soma += (entry/j);
			}
			j++;
		}
		if (j*j == entry)
			soma += j;
		cout << soma << endl;
	}	
    return 0;
}

