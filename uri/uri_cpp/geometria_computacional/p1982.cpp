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
	return (a.second < b.second);
}

int produtoCruzado(int x1, int y1, int x2, int y2);
double calculaAngulo(pair<int, int> pivo, pair<int, int> ponto);
int curva(pair<int, int> a, pair<int, int> b, pair<int, int> c);

int main() {
	int N, i, x, y, size;
	double d;
	vector< pair <int, int> > pontos;	
	vector< pair <double, int> > angulo;
	vector<int> pilha;
	pair <int, int> pivo;

	cin >> N;
	while (N > 0) {
		for (i = 0; i < N; i++) {
			cin >> x;
			cin >> y;	
			pontos.push_back(make_pair(x, y));	
		}
		/*for (i = 0; i < N; i++) {
			cout << pontos[i].first << " " << pontos[i].second << "|";
		}
		cout << endl;*/
		sort(pontos.begin(), pontos.end(), func);
		/*for (i = 0; i < N; i++) {
			cout << pontos[i].first << " " << pontos[i].second << "|";
		}
		cout << endl << endl;*/
		pivo = pontos[0];
		angulo.push_back(make_pair(0, 0));
		for (i = 1; i < N; i++) {
			angulo.push_back(make_pair(calculaAngulo(pivo, pontos[i]), i));
		}
		sort(angulo.begin(), angulo.end());
		/*cout << "a: ";		
		for (i = 0; i < N; i++) {
			cout << angulo[i].first << " [" << pontos[angulo[i].second].first << " " << pontos[angulo[i].second].second <<"]|";
		}
		cout << endl;*/
		pilha.push_back(0);
		pilha.push_back(angulo[1].second);
		for (i = 2; i < N; i++) {
			pilha.push_back(angulo[i].second);
			while (true) {
				size = pilha.size();
				if (size < 3)
					break;
				if (curva(pontos[pilha[size-3]], pontos[pilha[size-2]], pontos[pilha[size-1]]))
					pilha.erase(pilha.begin()+size-2);
				else
					break;
			}
		}
		/*cout << "p: ";
		for (i = 0; i < pilha.size(); i++) {
			cout << pontos[pilha[i]].first << " " << pontos[pilha[i]].second << "|";
		}
		cout << endl;*/
		
		d = 0;
		for (i = 1; i < pilha.size(); i++) {
			d += sqrt(pow(pontos[pilha[i]].first - pontos[pilha[i-1]].first, 2) + pow(pontos[pilha[i]].second - pontos[pilha[i-1]].second, 2));
		}
		d += sqrt(pow(pontos[pilha[pilha.size()-1]].first - pontos[pilha[0]].first, 2) + pow(pontos[pilha[pilha.size()-1]].second - pontos[pilha[0]].second, 2));
		
		printf("Tera que comprar uma fita de tamanho %.2f.\n", d);
		angulo.clear();
		pontos.clear();
		pilha.clear();
		cin >> N;
	}

	return 0;
}

int produtoCruzado(int x1, int y1, int x2, int y2) {
	return x1*y2 - x2*y1;
}

double calculaAngulo(pair<int, int> pivo, pair<int, int> ponto) {
	return atan2(ponto.second-pivo.second, ponto.first-pivo.first);
}

int curva(pair<int, int> a, pair<int, int> b, pair<int, int> c) {
	int d = produtoCruzado(b.first-a.first, b.second-a.second, c.first-b.first, c.second-b.second);
	if (d < 0)
		return 1;
	return 0;
}


