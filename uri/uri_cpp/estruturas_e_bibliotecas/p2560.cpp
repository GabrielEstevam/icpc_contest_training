#include <iostream>
#include <sstream>
#include <string>
#include <stdlib.h>
#include <stdio.h>
#include <math.h>
#include <vector>
#include <algorithm>
#include <queue>

using namespace std;

int main() {
	int N, B;
	int i, k, n;
	vector <int> listMax;
	vector <int> listMin;
	int score = 0, partialScore = 0;

	while (cin >> N) {
		cin >> B;
		k = 0;

		make_heap(listMax.begin(), listMax.end());
		make_heap(listMin.begin(), listMin.end());

		for (i = 0; i < N; i++) {
			cin >> n;
			partialScore += n;
			if (int(listMax.size()) < (B - 1)) {
				listMax.push_back(n);
				//push_heap(listMax.begin(), listMax.end());
				listMin.push_back(n*-1);
				//push_heap(listMin.begin(), listMin.end());
				cout << "listMax:";
				for (int j = 0; j < int(listMax.size()); j++) {
					cout << " " << listMax[j];
				}
				cout << endl;
			} else {
				cout << "max: " << listMax.front() << endl;
				cout << "min: " << listMin.front() << endl;
				cout << "listMax:";
				for (int j = 0; j < int(listMax.size()); j++) {
					cout << " " << listMax[j];
				}
				cout << endl;
				score += partialScore - listMax.front() + listMin.front();
				partialScore -= listMax[k];
				listMax[k] = n;
				listMin[k] = n*-1;
				k++;
				if (k == B)
					k = 0;
			}
		}
		cout << score << endl;
		listMax.clear();
		listMin.clear();
	}	

	

	/*int list[] = {9, 6, 7, 2, 3};
	vector <int> heap (list, list+5);

	make_heap(heap.begin(), heap.end());

	heap[0] = 8;
	cout << "s: " << heap.size() << endl;
	for (unsigned i = 0; i < 5; i++) {
		cout << heap.front() << endl;
		pop_heap(heap.begin(), heap.end());
		heap.pop_back();
	}*/

    return 0;
}
