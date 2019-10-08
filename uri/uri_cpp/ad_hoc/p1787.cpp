#include <iostream>
#include <sstream>
#include <string>
#include <stdlib.h>
#include <stdio.h>
#include <math.h>
#include <vector>

using namespace std;

int main() {
	int i, N, j;
	long long a, b, c, entryA, entryB, entryC, k = 2;
	bool fa, fb, fc;
	vector <long long> p;
	while (k <= 1000000000) {
		p.push_back(k);
		k *= 2;
	}
	cin >> N;
	while (N != 0) {
		a = 0;
		b = 0;
		c = 0;
		for (i = 0; i < N; i++) {
			scanf("%ld", &entryA);
			scanf("%ld", &entryB);
			scanf("%ld", &entryC);
			fa = 0;
			fb = 0;
			fc = 0;
			for (j = 0; j < p.size(); j++) {
				if (entryA == p[j])
					fa = 1;
				if (entryB == p[j])
					fb = 1;
				if (entryC == p[j])
					fc = 1;
			}
			if (fa)
				a++;
			if (fb)
				b++;
			if (fc)
				c++;
			if (entryA > entryB and entryA > entryC) {
				if (fa)
					a++;
			} else if (entryB > entryA and entryB > entryC) {
				if (fb)
					b++;
			} else if (entryC > entryA and entryC > entryB) {
				if (fc)
					c++;
			}
		}
		if (a > b and a > c) {
			printf("Uilton\n");
		} else if (b > a and b > c) {
			printf("Rita\n");
		} else if (c > a and c > b) {
			printf("Ingred\n");
		} else {
			printf("URI\n");
		}
		scanf("%d", &N);
	}
	return 0;
}
