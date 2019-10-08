#include <iostream>
#include <sstream>
#include <string>
#include <stdlib.h>
#include <stdio.h>
#include <math.h>
#include <vector>

using namespace std;

class A {
    public:
        int m;
        int n;
        int flag;
        int corte;
        int multiplicacoes;
        A(int M, int N);
};

A::A(int M, int N) {
    m = M;
    n = N;
    flag = 0;
    corte = -1;
    multiplicacoes = -1;
}

int minimizaMult(int i, int j, int Empate);
string printSaida(int i, int j, string saida);

vector <A> As;
vector < vector<A> > M;

int main()
{
    int N;
    cin >> N;
    int entrada1, entrada2;
    int mult = 0, Empate = 0;
    while (N > 0) {
        for (int i = 0; i < N; i++) {
            cin >> entrada1;
            cin >> entrada2;
            As.push_back(A(entrada1, entrada2));
        }
        for (int i = 0; i < N; i++) {
            vector <A> row;
            for (int j = i; j < N; j++)
                row.push_back(A(i, j));
            M.push_back(row);
        }

        Empate = minimizaMult(0, N-1, 0);

        if (Empate) {
            mult = 0;
            for (unsigned i = 0; i < M.size(); i++) {
                for (unsigned j = 0; j < M[i].size(); j++) {
                    if (M[i][j].multiplicacoes > mult)
                        mult = M[i][j].multiplicacoes;
                }
            }
            cout << mult << endl;
        } else {
            cout << "(" << printSaida(0, N-1, "") << ")" << endl;
        }
        As.clear();
        M.clear();

        cin >> N;
    }
    return 0;
}

int minimizaMult(int i, int j, int Empate){
    int mult;
    if (i == j) {
        M[i][j - i].multiplicacoes = 0;
        M[i][j - i].corte = i;
    } else {
        for (int k = i; k < j; k++) {
            if (M[i][k - i].flag == 0)
                Empate = minimizaMult(i, k, Empate);
            if (M[k + 1][j - (k + 1)].flag == 0)
                Empate = minimizaMult(k + 1, j, Empate);
            mult = M[i][k - i].multiplicacoes + M[k + 1][j - (k + 1)].multiplicacoes + As[i].m * As[k].n * As[j].n;
            if (mult < M[i][j - i].multiplicacoes || M[i][j - i].multiplicacoes == -1){
                M[i][j - i].multiplicacoes = mult;
                M[i][j - i].corte = k;
            } else if (mult == M[i][j - i].multiplicacoes)
                Empate = 1;
        }
    }
    M[i][j - i].flag = 1;
    return Empate;
}

string printSaida(int i, int j, string saida) {
    string saida1;
    string saida2;
    if (i == j) {
            string retorno;
            retorno = "A";
            ostringstream ss;
            ss << (i+1);
            string s = ss.str();
            retorno += s;
            return retorno;
    } else if (i+1 == j) {
            string retorno;
            retorno = "A";
            ostringstream ss;
            ss << (i+1);
            string s = ss.str();
            retorno += s;
            s = "A";
            retorno += s;
            ostringstream sss;
            sss << (j+1);
            s = sss.str();
            retorno += s;
            return retorno;
    } else {
        saida1 = printSaida(i, M[i][j - i].corte, saida);
        if (i != M[i][j-i].corte)
            saida1 = "("+saida1+")";
        saida2 = printSaida(M[i][j - i].corte + 1, j, saida);
        if (M[i][j-i].corte+1 != j)
            saida2 = "(" + saida2 + ")";
    }
    return saida1+saida2;
}
