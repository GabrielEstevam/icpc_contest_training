#include <iostream>
#include <sstream>
#include <string>
#include <stdlib.h>
#include <stdio.h>
#include <math.h>

using namespace std;

int main()
{
    int M, N, K, L, k, l, * Kx, * Ky, Lx, Ly, Distance, * Ix, * Iy, I = 1;

    cin >> M;
    while (M != 0) {
        cin >> N;
        cin >> K;
        Kx = (int*)malloc(sizeof(int)*K);
        Ky = (int*)malloc(sizeof(int)*K);
        for (k = 0; k < K; k++) {
            cin >> Kx[k];
            cin >> Ky[k];
        }
        cin >> L;
        Ix = (int*)malloc(sizeof(int)*L);
        Iy = (int*)malloc(sizeof(int)*L);
        for (l = 0; l < L; l++) {
            cin >> Lx;
            cin >> Ly;
            Distance = abs(Kx[0]-Lx)+abs(Ky[0]-Ly);
            Ix[l] = Kx[0];
            Iy[l] = Ky[0];
            for (k = 1; k < K; k++) {
                if (abs(Kx[k]-Lx)+abs(Ky[k]-Ly) < Distance) {
                    Distance = abs(Kx[k]-Lx)+abs(Ky[k]-Ly);
                    Ix[l] = Kx[k];
                    Iy[l] = Ky[k];
                } else if (abs(Kx[k]-Lx)+abs(Ky[k]-Ly) == Distance) {
                    if (Ky[k] < Iy[l] || (Ky[k] == Iy[l] && Kx[k] < Ix[l])) {
                        Ix[l] = Kx[k];
                        Iy[l] = Ky[k];
                    }
                }
            }
        }
        if (L != 0)
            cout << "Instancia " << I++ << endl;
        for (l = 0; l < L; l++)
            cout << Ix[l] << " " << Iy[l] << endl;
        cin >> M;
    }

    return 0;
}
