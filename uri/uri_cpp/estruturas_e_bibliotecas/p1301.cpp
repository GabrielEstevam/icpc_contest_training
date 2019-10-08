// Segment tree positive/negative/null
#include <iostream>
#include <sstream>
#include <string>
#include <stdlib.h>
#include <stdio.h>
#include <vector>
#include <math.h>

using namespace std;

void update (vector < int > * t, int i, int x, int N);
int query (vector < int > * t, int x, int y, int N, int v, int a, int b);
void firstUpdate (vector <int> * t, int N, int x);

int main() {
    int N, Q, i, j, entry, index, x, y, r, K;
    char c;
    vector < int > t; //segment tree
    
    while (cin >> N) {
        scanf("%d", &Q);
        K = pow(2, ceil(log(N)/log(2)));
        for (i = 0; i < 2*K; i++) {
            t.push_back(-101);
        }
        for (i = 1; i <= N; i++) {
            scanf("%d", &entry);
            if (entry < 0) {
                t[K-1+i] = -1;
            } else if (entry > 0) {
                t[K-1+i] = 1;
            } else {
                t[K-1+i] = 0;
            }     
        }
        firstUpdate(&t, K, 1);
        /*for (i = 1; i < 2*K; i++)
            cout << t[i] << " ";
        cout << endl;*/
        
        for (i = 0; i < Q; i++) {
            scanf(" %c", &c);
            if (c == 'C') {
                scanf("%d", &index);
                scanf("%d", &x);
                update(&t, index, x, K);
                /*for (j = 1; j < 2*K; j++)
                    cout << t[j] << " ";
                cout << endl;*/
            } else if (c == 'P') {
                scanf("%d", &x);
                scanf("%d", &y);
                r = query(&t, x, y, K, 1, 1, K);
                if (r == 0) {
                    printf("0");
                } else if (r > 0) {
                    printf("+");
                } else {
                    printf("-");
                }
            }
        }
        printf("\n");
        t.clear();
    }
    return 0;
}

void update (vector < int > * t, int i, int x, int N) {
    int j = N-1+i;
    if (x > 0) {
        t->at(j) = 1;
    } else if (x < 0) {
        t->at(j) = -1;
    } else {
        t->at(j) = 0;
    }
    do {
        j = j/2;
        if (t->at(j*2) == -101) {
            t->at(j) = t->at(j*2+1);
        } else if (t->at(j*2+1) == -101) {
            t->at(j) = t->at(j*2);
        } else {
            t->at(j) = t->at(j*2)*t->at(j*2+1);
        }
    } while (j > 1);
}

int query (vector < int > * t, int x, int y, int N, int v, int a, int b) {
    if (a == x and b == y) {
        return t->at(v);
    } else {
        int mid = (b + a - 1)/2;
        if (y <= mid) {
            return query(t, x, y, N, v*2, a, mid);
        } else if (x > mid) {
            return query(t, x, y, N, v*2+1, mid+1, b);
        } else {
            int right = query(t, x, mid, N, v*2, a, mid);
            int left = query(t, mid+1, y, N, v*2+1, mid+1, b);
            if (right == 0 or left == 0) {
                return 0;
            } else {
                return right*left;
            }
        }
    }
    
    return 0;
}

void firstUpdate(vector <int> * t, int N, int x) {
    if (x < N) {
        firstUpdate(t, N, x*2);
        firstUpdate(t, N, x*2+1);
        if (t->at(x*2) == -101) {
            t->at(x) = t->at(x*2+1);
        } else if (t->at(x*2+1) == -101) {
            t->at(x) = t->at(x*2);
        } else {
            t->at(x) = t->at(x*2)*t->at(x*2+1);
        }
    }
}