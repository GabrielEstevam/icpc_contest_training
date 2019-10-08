#include <iostream>
#include <sstream>
#include <string>
#include <stdlib.h>
#include <stdio.h>
#include <math.h>
#include <vector>
#include <bitset>

using namespace std;

int main() {
	unsigned long i, j, k;
	unsigned long N, num;	
	unsigned long entry;	
	//vector <unsigned long> numero;
	vector < bitset<1> > flag;
	
	//N = 1000000000000000000;
	N = 1000000000; 	
	for (i = 0; i <= N; i++)
		flag.push_back(1);
	cout << "oi" << endl;
	for (i = 2; i <= N; i++) {
		if (flag[i] == 1) {
			num = i;			
			num += num;
			while (num <= N) {
				flag[num] = false;
				num += num;
			}
		}
	}
	cout << "oi" << endl;
	/*cin >> entry;
	while (entry != 0) {
		cout << entry << " = ";		
		j = 3;		
		k = 0;
		while (k < 3) {
			if (flag[j]) {
				if (entry % j == 0) {
					entry = entry/j;
					cout << j;
					k++;
					if (k < 3)
						cout << " x ";
				}
			}
			j++;
		}
		cout << endl;
		cin >> entry;
	}*/
	flag.clear();
    return 0;
}
