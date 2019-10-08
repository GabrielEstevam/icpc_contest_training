#include <iostream>
#include <sstream>
#include <string>
#include <stdlib.h>
#include <stdio.h>
#include <math.h>
#include <vector>

using namespace std;


int main() {
	int i, N;
	while (cin >> N){
		vector <int> primos;
		primos.push_back(2);
		primos.push_back(3);
		primos.push_back(5);
		for (i = 7; i < N; i++) {
			if (i % 2 != 0 and i % 3 != 0 and i % 5 != 0) 			
				primos.push_back(i);
		}
		cout << primos.size() << endl;
		//for (i = 0; i < primos.size(); i++)
		//	cout << primos[i] << " ";
		//cout << endl;
	}	
    return 0;
}

