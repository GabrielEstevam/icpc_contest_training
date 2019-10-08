#include <iostream>
#include <sstream>
#include <string>
#include <stdlib.h>
#include <stdio.h>
#include <vector>
#include <stdio.h>
#include <unistd.h>

using namespace std;

int main() {
    int i, t, l = 0, j, k = 0;
    char c;
    string entry;
    vector < vector <char> > v;
    vector <char> row;
    v.push_back(row);
    bool home = true;

    c = getchar();
    while (1) {
        if (c != 10 and c != -1) {
            if (c == '[') {
                home = false;
                vector <char> row;
                v.push_back(row);
                l++;
            } else if (c == ']') {
                home = true;
            } else {
                if (home) {
                    v[0].push_back(c);
                } else {
                    v[l].push_back(c);
                }
                k++;
            }
        } else {
            if (k > 0) {
                char saida[k+1];
                k = 0;
                for (i = l; i >= 0; i--) {
                    for (j = 0; j < v[i].size(); j++) {
                        saida[k++] = v[i][j];
                    }
                }
                saida[k] = '\0';
                printf("%s\n", saida);
            }
            v.clear();
            vector <char> row;
            v.push_back(row);
            l = 0;
            k = 0;
        }
        if (c == -1)
            break;
        c = getchar();
    }

    return 0;
}