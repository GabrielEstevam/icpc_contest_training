#include <iostream>
#include <sstream>
#include <string>
#include <stdlib.h>
#include <stdio.h>
#include <math.h>
#include <vector>

using namespace std;

int main() {
   	unsigned long long int i, N, in, soma = 0, soma_aux = 0, roubadas = 0, atacadas = 0;
	bool flag = true;

	cin >> N;
	
	for (i = 0; i < N; i++) {
		cin >> in;
		soma += in;
		if (flag) {
			if (in % 2 == 1) {
				atacadas++;
				roubadas++;
				if (in > 1)
					soma_aux++;
			} else {
				atacadas++;
				roubadas++;
				roubadas += soma_aux;
				flag = false;
			}
		}
	}
	
	cout << atacadas << " " << (soma - roubadas) << endl;
    return 0;
}
