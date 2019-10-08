#include <iostream>
#include <sstream>
#include <string>
#include <stdlib.h>
#include <stdio.h>
#include <vector>

using namespace std;

int main()
{
    int x, y;
    int i, j;
    char c, direcao;
    vector < vector<char> > entry;
    vector < vector<char> > mapa;

    cin >> x;
    cin >> y;

    for (i = 0; i < y; i++) {
        vector <char> row1;
        entry.push_back(row1);
        vector <char> row2;
        mapa.push_back(row2);
        for (j = 0; j < x; j++) {
            cin >> c;
            entry[i].push_back(c);
            mapa[i].push_back('.');
        }
    }

    i = 0;
    j = 0;
    direcao = 'C';
    while (true) {
        if (mapa[j][i] == '!') {
            cout << '!' << endl;
            break;
        }
        if (entry[j][i] == '>') {
            direcao = 'L';
            mapa[j][i] = '!';
        } else if (entry[j][i] == '<') {
            direcao = 'O';
            mapa[j][i] = '!';
        } else if (entry[j][i] == '^') {
            direcao = 'S';
            mapa[j][i] = '!';
        } else if (entry[j][i] == 'v') {
            direcao = 'N';
            mapa[j][i] = '!';
        } else if (entry[j][i] == '*') {
            cout << '*' << endl;
            break;
        }

        if (direcao == 'L') {
            if (i + 1 < x) {
                i += 1;
            } else {
                cout << '!' << endl;
                break;
            }
        } else if (direcao == 'O') {
            if (i - 1 >= 0) {
                i -= 1;
            } else {
                cout << '!' << endl;
                break;
            }
        } else if (direcao == 'N') {
            if (j + 1 < y) {
                j += 1;
            } else {
                cout << '!' << endl;
                break;
            }
        } else if (direcao == 'S') {
            if (j - 1 >= 0) {
                j -= 1;
            } else {
                cout << '!' << endl;
                break;
            }
        }
    }


    return 0;
}
