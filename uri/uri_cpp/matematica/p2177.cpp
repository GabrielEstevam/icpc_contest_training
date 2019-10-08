#include <iostream>
#include <sstream>
#include <string>
#include <stdlib.h>
#include <stdio.h>
#include <math.h>
#include <vector>

using namespace std;

int main() {
    int xi, yi, n, i, x, y, t;
    bool flag = false;
    scanf("%d", &xi);
    scanf("%d", &yi);
    scanf("%d", &n);
    for (i = 0; i < n; i++) {
        scanf("%d", &x);
        scanf("%d", &y);
        scanf("%d", &t);
        if ((x-xi)*(x-xi) + (y-yi)*(y-yi) < t*t) {
            if (flag) {
                printf(" %d", i+1);
            } else {
                printf("%d", i+1);
                flag = true;
            }
        }
    }
    if (flag == false)
        printf("-1");
    printf("\n");

    return 0;
}
