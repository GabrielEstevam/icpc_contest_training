#include <iostream>
#include <sstream>
#include <string>
#include <stdlib.h>
#include <stdio.h>
#include <math.h>
#include <vector>

using namespace std;

int bfs(int x1, int y1, int x2, int y2);
int convert(char c);

int main() {
	string c1, c2, s;
	int x1, y1, x2, y2;
	while (cin >> c1) {
		cin >> c2;
		x1 = convert(c1[0]);	
		s = c1[1];
		y1 = atoi(s.c_str()) - 1;
		x2 = convert(c2[0]);
		s = c2[1];		
		y2 = atoi(s.c_str()) - 1;
		//cout << x1 << " " << y1 << " " << x2 << " " << y2 << endl;
		cout << "To get from " << c1 << " to " << c2 << " takes " << bfs(x1, y1, x2, y2) << " knight moves." << endl;
	}

    return 0;
}

int bfs (int x1, int y1, int x2, int y2) {	
	int i, j, k;
	int N = 64, n = 8;
	bool flag;
	vector < vector<int> > D;
	for (i = 0; i < N; i++) {
		vector <int> row;
		D.push_back(row);
		for (j = 0; j < N; j++) 
			D[i].push_back(10000);
	}
	D[x1][y1] = 0;
	vector < vector<int> > fila;
	vector <int> row;
	row.push_back(x1);
	row.push_back(y1);
	fila.push_back(row);
	while (fila.size() > 0) {	
		i = fila[0][0];
		j = fila[0][1];
		fila.erase(fila.begin());
		if (i == x2 and j == y2)
			return D[i][j];
		////
		if (i+2 < n) {
			if (j+1 < n) {				
				if (D[i+2][j+1] > D[i][j] + 1) {
					D[i+2][j+1] = D[i][j] + 1;
					vector <int> row;
					row.push_back(i+2);
					row.push_back(j+1);
					fila.push_back(row);
				}
			}
			if (j-1 >= 0) {				
				if (D[i+2][j-1] > D[i][j] + 1) {
					D[i+2][j-1] = D[i][j] + 1;
					vector <int> row;
					row.push_back(i+2);
					row.push_back(j-1);
					fila.push_back(row);
				}
			}
		}
		////				
		if (i-2 >= 0) {
			if (j+1 < n) {				
				if (D[i-2][j+1] > D[i][j] + 1) {
					D[i-2][j+1] = D[i][j] + 1;
					vector <int> row;
					row.push_back(i-2);
					row.push_back(j+1);
					fila.push_back(row);
				}
			}
			if (j-1 >= 0) {				
				if (D[i-2][j-1] > D[i][j] + 1) {
					D[i-2][j-1] = D[i][j] + 1;
					vector <int> row;
					row.push_back(i-2);
					row.push_back(j-1);
					fila.push_back(row);
				}
			}
		}
		////
		if (j+2 < n) {
			if (i+1 < n) {				
				if (D[i+1][j+2] > D[i][j] + 1) {
					D[i+1][j+2] = D[i][j] + 1;
					vector <int> row;
					row.push_back(i+1);
					row.push_back(j+2);
					fila.push_back(row);
				}
			}
			if (i-1 >= 0) {				
				if (D[i-1][j+2] > D[i][j] + 1) {
					D[i-1][j+2] = D[i][j] + 1;
					vector <int> row;
					row.push_back(i-1);
					row.push_back(j+2);
					fila.push_back(row);
				}
			}
		}
		////
		if (j-2 >= 0) {
			if (i+1 < n) {				
				if (D[i+1][j-2] > D[i][j] + 1) {
					D[i+1][j-2] = D[i][j] + 1;
					vector <int> row;
					row.push_back(i+1);
					row.push_back(j-2);
					fila.push_back(row);
				}
			}
			if (i-1 >= 0) {				
				if (D[i-1][j-2] > D[i][j] + 1) {
					D[i-1][j-2] = D[i][j] + 1;
					vector <int> row;
					row.push_back(i-1);
					row.push_back(j-2);
					fila.push_back(row);
				}	
			}
		}
	}
	return D[x2][y2];
}

int convert(char c) {
	switch (c) {
		case 'a':
			return 0;
		case 'b':
			return 1;
		case 'c':
			return 2;
		case 'd':
			return 3;
		case 'e':
			return 4;
		case 'f':
			return 5;
		case 'g':
			return 6;
		case 'h':
			return 7;	
	}
}
