#include <iostream>
#include <sstream>
#include <string>
#include <stdlib.h>
#include <stdio.h>
#include <math.h>
#include <vector>

using namespace std;

int buscaLargura (int O, int D, int K);

int main() {
	int O, D, K;

	cin >> O;
	cin >> D;
	cin >> K;

	while (O != 0 or D != O or K != 0) {
		cout << buscaLargura(O, D, K) << endl;
		cin >> O;
		cin >> D;
		cin >> K;
	}

    return 0;
}

int buscaLargura (int O, int D, int K) {
	int i, entry, c;	
	vector <bool> flag;
	for (i = 0; i <= 100000; i++)
		flag.push_back(true);
	for (i = 0; i < K; i++) {
		cin >> entry;
		flag[entry] = false;
	}
	vector < vector<int> > fila;
	vector <int> A, B;
	A.push_back(O);
	A.push_back(0);
	B.push_back(0);
	B.push_back(0);
	flag[O] = false;
	fila.push_back(A);
	int k = 0;
	while (fila.size() > 0) {
		A = fila[0];
		//cout << "k: " << ++k << endl;		
		cout << "A: " << A[0] << endl;
		fila.erase(fila.begin());
		// botao (-1)
		c = A[0] - 1;
		if (c > 0) {
			if (flag[c]) {
				if (c == D) {
					return A[1] + 1;
				} else {
					flag[c] = false;
					B[0] = c;
					B[1] = A[1] + 1;
					fila.push_back(B);
				}					
			}
		}
		// botao (+1)
		c = A[0] + 1;
		if (c <= 100000) {
			if (flag[c]) {
				if (c == D) {
					return A[1] + 1;
				} else {
					flag[c] = false;
					B[0] = c;
					B[1] = A[1] + 1;
					fila.push_back(B);
				}					
			}
		}
		// botao (/2)
		if (A[0] % 2 == 0) {
			c = A[0]/2;
			if (c > 0) {
				if (flag[c]) {
					if (c == D) {
						return A[1] + 1;
					} else {
						flag[c] = false;
						B[0] = c;
						B[1] = A[1] + 1;
						fila.push_back(B);
					}					
				}
			}
		}
		// botao (*2)
		c = A[0] * 2;
		if (c <= 100000) {
			if (flag[c]) {
				if (c == D) {
					return A[1] + 1;
				} else {
					flag[c] = false;
					B[0] = c;
					B[1] = A[1] + 1;
					fila.push_back(B);
				}					
			}
		}
		// botao (*3)
		c = A[0] * 3;
		if (c <= 100000) {
			if (flag[c]) {
				if (c == D) {
					return A[1] + 1;
				} else {
					flag[c] = false;
					B[0] = c;
					B[1] = A[1] + 1;
					fila.push_back(B);
				}					
			}
		}		
	}
	flag.clear();
	fila.clear();
	return -1;
}
