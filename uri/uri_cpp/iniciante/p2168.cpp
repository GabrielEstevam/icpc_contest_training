#include <iostream>
#include <sstream>
#include <string>
#include <stdlib.h>
#include <stdio.h>
#include <math.h>
#include <vector>

using namespace std;

int main() {
   	int n, entry, i, j;
	vector < vector <int> > M;
	cin >> n;
	n++;
	for (i = 0; i < n; i++) {
		vector <int> row;		
		for (j = 0; j < n; j++) {
			cin >> entry;
			row.push_back(entry);
		}
		M.push_back(row);
	}
	for (i = 1; i < n; i++) {
		for (j = 1; j < n; j++) {
			if (M[i-1][j-1] + M[i][j-1] + M[i-1][j] + M[i][j] >= 2)
				cout << "S";
			else
				cout << "U";
		}
		cout << endl;
	}
    return 0;
}
