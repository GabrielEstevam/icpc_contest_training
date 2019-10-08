#include <iostream>
#include <sstream>
#include <string>
#include <stdlib.h>
#include <stdio.h>
#include <vector>

using namespace std;

int main() {
    int n, d, i, j;
    unsigned k;
    string entry;
    vector <char> input;

    cin >> n;
    cin >> d;

    while (n != 0) {
        cin >> entry;
        for (k = 0; k < entry.size(); k++)
            input.push_back(entry[k]);
        i = 0;
        j = 1;
        while (i < d) {
            if (input[j] > input[j-1]) {
                input.erase(input.begin()+j-1);
                i++;
                if (j > 1)
                    j--;
            } else if (j+1 < input.size()) {
                j++;
            } else {
                while (i < d) {
                    input.pop_back();
                    i++;
                }
            }
        }
        for (k = 0; k < input.size(); k++)
            cout << input[k];
        cout << endl;
        input.clear();
        cin >> n;
        cin >> d;
    }

    return 0;
}
