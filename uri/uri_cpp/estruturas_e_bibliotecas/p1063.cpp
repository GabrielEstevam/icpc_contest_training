#include <iostream>
#include <sstream>
#include <string>
#include <stdlib.h>
#include <stdio.h>
#include <vector>

using namespace std;

int main() {
    int N, i;
    char e1, e2;
    cin >> N;

    while (N != 0) {
        vector <char> entry1;
        entry1.push_back('-');
        for (i = 0; i < N; i++) {
            scanf(" %c", &e1);
            if (e1 >= 97 and e1 <= 122)
                entry1.push_back(e1);
        }
        vector <char> entry2;
        entry2.push_back('-');
        for (i = 0; i < N; i++) {
            scanf(" %c", &e2);
            if (e2 >= 97 and e2 <= 122)
                entry2.push_back(e2);
        }
        vector <char> stack;
        stack.push_back('-');
        stack.push_back(entry1[1]);
        entry1.erase(entry1.begin()+1);
        string out = "I";
        while (true) {
            if (stack[stack.size()-1] == entry2[1]) {
                out += 'R';
                stack.pop_back();
                entry2.erase(entry2.begin()+1);
            } else {
                if (entry1.size() == 1)
                    break;
                stack.push_back(entry1[1]);
                entry1.erase(entry1.begin()+1);
                out += 'I';
            }
            if (entry2.size() == 1)
                break;
        }
        if (entry2.size() == 1) {
            cout <<out << endl;
        } else {
            cout << out << " Impossible" << endl;
        }
        cin >> N;
    }
    return 0;
}