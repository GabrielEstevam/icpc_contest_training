#include <iostream>
#include <sstream>
#include <string>
#include <stdlib.h>
#include <stdio.h>
#include <algorithm>

using namespace std;

int rec(int pos, int n, long long cont);

int main() {
    int N;
    while (cin >> N)
    	printf("%d\n", rec(2, N, 1));
    return 0;
}

int rec(int pos, int n, long long cont) {
	if (pos == 1)
		return cont;
	if (pos <= n/2)
		return rec(pos*2, n, cont+1);
	return rec((pos-n/2-1)*2+1, n, cont+1);
}
