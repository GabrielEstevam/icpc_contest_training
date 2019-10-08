#include <iostream>
#include <sstream>
#include <string>
#include <stdlib.h>
#include <stdio.h>
#include <math.h>
#include <vector>

using namespace std;

int main() {

	int N, AAH, xc, yc, lc, x, y, l, i, j, n;
	double d, ds;
	vector <double> xs1, ys1, xs2, ys2;
	bool flag = true;

	for (i = 0; i < 4; i++) {
		xs1.push_back(0);
		ys1.push_back(0);
		xs2.push_back(0);
		ys2.push_back(0);
	}

	cin >> N;
	cin >> AAH;
	cin >> xc;
	cin >> yc;
	cin >> lc;

	xs1[0] = (double) xc - lc/2.0;
	xs1[1] = (double) xc - lc/2.0;
	xs1[2] = (double) xc + lc/2.0;
	xs1[3] = (double) xc + lc/2.0;
	ys1[0] = (double) yc - lc/2.0;
	ys1[1] = (double) yc + lc/2.0;
	ys1[2] = (double) yc - lc/2.0;
	ys1[3] = (double) yc + lc/2.0;

	for (n = 1; n < N; n++) {
		cin >> x;
		cin >> y;
		cin >> l;
		if (flag) {
			xs2[0] = (double) x - l/2.0;
			xs2[1] = (double) x - l/2.0;
			xs2[2] = (double) x + l/2.0;
			xs2[3] = (double) x + l/2.0;
			ys2[0] = (double) y - l/2.0;
			ys2[1] = (double) y + l/2.0;
			ys2[2] = (double) y - l/2.0;
			ys2[3] = (double) y + l/2.0;

			d = sqrt(pow(xs1[0] - xs2[0], 2) + pow(ys1[0] - ys2[0], 2));
			for (i = 0; i < 4; i++) {
				for (j = 0; j < 4; j++) {
					 ds = sqrt(pow(xs1[i] - xs2[j], 2) + pow(ys1[i] - ys2[j], 2));
					 if (ds < d) {
					 	d = ds;
					 }
				}
			}
			if (d > AAH) {
				if (((x - l) > (xc - lc) and (x + l) < (xc + lc)) or ((y - l) > (yc - lc) and (y + l) < (yc + lc))) {
				} else if (((x - l) < (xc - lc) and (x + l) > (xc + lc)) or ((y - l) < (yc - lc) and (y + l) > (yc + lc))) {
				} else {
					flag = false;
			}	}
			xc = x;
			yc = y;
			lc = l;
			for (i = 0; i < 4; i++) {
				xs1[i] = xs2[i];
				ys1[i] = ys2[i];
			}
		}
	}
	if (flag) {
		cout << "YEAH" << endl;
	} else {
		cout << "OUCH" << endl;
	}
    return 0;
}
