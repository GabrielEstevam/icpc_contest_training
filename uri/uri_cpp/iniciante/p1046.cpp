#include <iostream>
#include <sstream>
#include <string>
#include <stdlib.h>
#include <stdio.h>

using namespace std;

int main()
{
    int inicio, fim, duracao;

    cin >> inicio;
    cin >> fim;

    duracao = fim - inicio;
    if (duracao <= 0)
        duracao += 24;

    cout << "O JOGO DUROU " << duracao <<" HORA(S)" << endl;

    return 0;
}
