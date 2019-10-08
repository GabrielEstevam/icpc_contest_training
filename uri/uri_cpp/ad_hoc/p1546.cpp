#include <iostream>
#include <sstream>
#include <string>
#include <stdlib.h>
#include <stdio.h>

using namespace std;

int main()
{
    int dias, k, feedback, i, j;

    cin >> dias;
    for (i = 0; i < dias; i++) {
        cin >> k;
        for (j = 0; j < k; j++) {
            cin >> feedback;
                switch (feedback) {
                    case 1:
                        cout << "Rolien" << endl;
                        break;
                    case 2:
                        cout << "Naej" << endl;
                        break;
                    case 3:
                        cout << "Elehcim" << endl;
                        break;
                    case 4:
                        cout << "Odranoel" << endl;
                        break;
                }
        }
    }

    return 0;
}
