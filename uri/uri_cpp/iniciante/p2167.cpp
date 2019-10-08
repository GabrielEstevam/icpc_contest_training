#include <iostream>
#include <sstream>
#include <string>
#include <stdlib.h>
#include <stdio.h>
#include <math.h>
#include <vector>

using namespace std;

int main() {
   	int n, entry1, entry2, i, saida = 0;
	bool flag = true;
	cin >> n;
	cin >> entry1;
	for (i = 1; i < n; i++) {
		cin >> entry2;
		if (flag and entry2 < entry1) {
			saida = i+1;
			flag = false;
		}
		entry1 = entry2;
	}
	cout << saida << endl;
    return 0;
}
