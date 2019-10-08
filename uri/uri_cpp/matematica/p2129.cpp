#include <iostream>
#include <sstream>
#include <string>
#include <stdlib.h>
#include <stdio.h>
#include <math.h>
#include <vector>

using namespace std;


int main() {
	int i, k = 1, n, N = 1000000;
	vector <int> fat;
	fat.push_back(1);
	long fatorial = 1, mod = 1000000000;
	for (i = 1; i <= N; i++) {
		fatorial = (fatorial*i) % mod;
		while (fatorial % 10 == 0)
			fatorial /= 10;
		fat.push_back(fatorial % 10);
	}
	while (cin >> n)
		cout << "Instancia " << k++ << endl << fat[n] << endl << endl;

    return 0;
}

