#include <stdio.h>

int main() {
	int k, i, r, N;
	short mod;
	r = scanf("%d", &k);
	for (i = 0; i < k; i++) {	
		r = scanf("%d", &N);
		mod = N % 4;
		if (mod == 0)
			printf("1\n");
		else if (mod == 1)
			printf("7\n");
		else if (mod == 2)
			printf("9\n");
		else
			printf("3\n");
	}
    return 0;
}
