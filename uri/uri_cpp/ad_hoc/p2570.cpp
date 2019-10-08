#include <iostream>
#include <sstream>
#include <string>
#include <stdlib.h>
#include <stdio.h>
#include <math.h>
#include <vector>
#include <bits/stdc++.h>

using namespace std;

bool func(const pair<int, int> &a, const pair<int, int> &b) {
	return (a.second > b.second);
}

int main() {
	int N, M, K, i, j, k, t = 0, x, y, l = 0, c = 0, aux;
	char entry;
	vector < pair <int, int> > lc;
	vector <int> player;

	cin >> N;
	cin >> M;
	cin >> K;
	
	for (i = 0; i < 4; i++) {
		player.push_back(0);
	}	
	for (i = 0; i < N+M; i++) {
		lc.push_back(make_pair(-1, -1));
	}

	for (k = 0; k < K; k++) {
		cin >> entry;
		if (entry == 'L') {
			cin >> x;
			x--;
			lc[x].first = k % 4;
			lc[x].second = t;
			t++;
		} else {
			cin >> y;
			y--;
			lc[N+y].first = 4 + (k % 4);
			lc[N+y].second = t;
			t++;
		}
			
	}
	sort(lc.begin(), lc.end(), func);
	
	for (i = 0; i < N+M; i++) {
		if (lc[i].first < 0)
			break;
		aux = lc[i].first;
		if (aux > 3) {
			c++;
			player[aux % 4] += (N - l);
		} else {
			l++;
			player[aux] += (M - c);
		}
	}

	cout << "R" << player[0] << " H" << player[1] << " C" << player[2] << " P" << player[3] << endl;
    	return 0;
}
