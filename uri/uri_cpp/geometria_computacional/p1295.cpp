#include <iostream>
#include <sstream>
#include <string>
#include <stdlib.h>
#include <stdio.h>
#include <math.h>
#include <vector>
#include <algorithm>

using namespace std;

double closestPair(int a, int b);
vector < vector <double> > pontos;

int main() {
	int N, i;
	double entry1, entry2;
	double d = 0;

	cin >> N;
	while (N > 0) {
		for (i = 0; i < N; i++) {
			cin >> entry1;
			cin >> entry2;
			vector <double> row;
			row.push_back(entry1);
			row.push_back(entry2);
			pontos.push_back(row);
		}
		sort(pontos.begin(), pontos.end());
		/*for (i = 0; i < N; i++) {
			cout << pontos[i][0] << " " << pontos[i][1] << endl;
		}*/
		d = closestPair(0, N);
		cout << d << endl;
		if (d < 10000) {
			printf("%.4f\n", d);
		} else {
			cout << "INFINITY" << endl;
		}


		cin >> N;	
	}
	pontos.clear();
	return 0;
}

double closestPair(int a, int b) {	
	if (b - a == 3) {
		double d1_2, d1_3, d2_3;
		d1_2 = sqrt(pow(pontos[a][0]-pontos[a+1][0], 2) + pow(pontos[a][1]-pontos[a+1][1], 2));
		d1_3 = sqrt(pow(pontos[a][0]-pontos[a+2][0], 2) + pow(pontos[a][1]-pontos[a+2][1], 2));
		d2_3 = sqrt(pow(pontos[a+1][0]-pontos[a+2][0], 2) + pow(pontos[a+1][1]-pontos[a+2][1], 2));
		cout << "d1 " << d1_2 << endl;
		cout << "d2 " << d1_3 << endl;
		cout << "d3 " << d2_3 << endl;		
		if (d1_2 <= d1_3 and d1_2 <= d2_3) {
			return d1_2;
		} else if (d1_3 <= d1_2 and d1_3 <= d2_3) {
			return d1_3;
		} else {
			return d2_3;
		}
	} else if (b - a == 2) {
		return sqrt(pow(pontos[a][0]-pontos[a+1][0], 2) + pow(pontos[a][1]-pontos[a+1][1], 2));
	} else if (b - a <= 1) {
		return 10000;
	} else {
		int i = 0, j = 0;
		double delta = (pontos[b-1][0] - pontos[a][0])/2;
		double d1, d2, dmin, d;		
		for (i = a; i < b; i++) {
			if (pontos[i][0] >= pontos[a][0] + delta) {
				break;
			}
		}
		d1 = closestPair(a, i);
		d2 = closestPair(i, b);
		if (d1 <= d2) {
			dmin = d1;
		} else {
			dmin = d2;
		}
		if (b - a < 16) {
			for (i = a; i < b; i++) {
				for (j = a; j < b; j++) {
					if (i != j) {
						d = sqrt(pow(pontos[i][0]-pontos[j][0], 2) + pow(pontos[i][1]-pontos[j][1], 2));
						if (d < dmin) {
							dmin = d;
						}
					}
				}
			}
		} else {
			for (i = a; i < a+16; i++) {
				for (j = a; j < a+16; j++) {
					if (i != j) {
						d = sqrt(pow(pontos[i][0]-pontos[j][0], 2) + pow(pontos[i][1]-pontos[j][1], 2));
						if (d < dmin) {
							dmin = d;
						}
					}
				}
			}
		}
	}
}
