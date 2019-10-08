#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    int N, i, entry, nTiras;
	double corte, A, soma;
	vector <int> tira;	

	cin >> N;
	cin >> A;
		
	while (N != 0 and A != 0) {
		for (i = 0; i < N; i++) {
			cin >> entry;
			tira.push_back(entry);
		}
		sort(tira.rbegin(), tira.rend());
		nTiras = 0;
		soma = 0;
		corte = 0; 
		for (i = 0; i < N - 1; i++) {
			nTiras++;
			soma += (tira[i] - tira[i+1]) * nTiras;
			corte = tira[i+1];
			if (soma >= A)
				break;
		}	
		if (soma < A) {
			nTiras++;
			soma += tira[N-1] * nTiras;
			corte = 0;
		}
		if (soma == A and corte == 0) {
			cout << ":D" << endl;
		} else if (soma < A){
			cout << "-.-" << endl;		
		} else {
			corte += (soma - A)/nTiras;
			printf("%.4f\n", corte);
		}
		tira.clear();
		cin >> N;
		cin >> A;
	}
    return 0;
}
