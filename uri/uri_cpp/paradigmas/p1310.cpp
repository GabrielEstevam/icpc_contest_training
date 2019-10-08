#include <iostream>
#include <vector>

using namespace std;

int main() {
	int N, i, j, entry, lucro, custo, maior;
	vector <int> receita;
	while (cin >> N) {
		cin >> custo;
		for (i = 0; i < N; i++) {
			cin >> entry;
			receita.push_back(entry);
		}
		maior = 0;
		for (i = 0; i < N; i++) {
			lucro = 0;
			for (j = i; j < N; j++) {
				lucro += (receita[j] - custo);
				if (lucro > maior)
					maior = lucro; 
			}	
		}
		receita.clear();
		cout << maior << endl;
	}

    return 0;
}
