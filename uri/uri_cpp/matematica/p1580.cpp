#include <iostream>
#include <sstream>
#include <string>
#include <stdlib.h>
#include <stdio.h>
#include <math.h>
#include <vector>
#include <algorithm>

using namespace std;


int main() {
	int i, k = 1, n, N = 1000;
	vector <long> fat;
	fat.push_back(1);
	for (i = 1; i <= N; i++)
		fat.push_back(fat[i-1]*i % 1000000007);
	//for (i = 0; i <= N; i++) {
	//	cout << i << "  " << fat[i] << endl;	
	//}
	string entry;
	vector <char> letras;
	long num;  
	int repete;
	while (cin >> entry) {
		n = entry.size();
		for (i = 0; i < n; i++)
			letras.push_back(entry[i]);
		sort(letras.begin(), letras.end());
		for (i = 0; i < n; i++)
			cout << letras[i];
		cout << endl;
		num = fat[letras.size()];		
		repete = 1;		
		for (i = 1; i < n; i++) {
			if (letras[i] != letras[i-1]) {				
				num /= fat[repete];
				cout << "r: " << repete << endl;
				cout << "n: " << num << endl;
				repete = 1;
			} else {
				repete++;			
			}
		}
		num /= fat[repete];
		printf("%ld\n", (num) % 1000000007);
	}
    return 0;
}
