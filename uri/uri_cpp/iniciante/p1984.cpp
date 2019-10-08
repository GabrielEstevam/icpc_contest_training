#include <iostream>
#include <sstream>
#include <string>
#include <stdlib.h>
#include <stdio.h>
#include <math.h>
#include <vector>

using namespace std;

int main() {
   	string entry;
	cin >> entry;
	int size = entry.size();
	for (int i = 0; i < size; i++)
		cout << entry[size - 1 - i];
	cout << endl;
    return 0;
}
