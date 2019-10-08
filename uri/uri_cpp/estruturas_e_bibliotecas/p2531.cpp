//Segment tree min-max
#include <iostream>
#include <sstream>
#include <string>
#include <stdlib.h>
#include <stdio.h>
#include <vector>
#include <math.h>

using namespace std;

void updateTmin (vector < int > * t, int i, int x, int N);
void updateTmax (vector < int > * t, int i, int x, int N);
int queryMin (vector < int > * t, int x, int y, int N, int v, int a, int b);
int queryMax (vector < int > * t, int x, int y, int N, int v, int a, int b);
void firstUpdateTmin (vector <int> * t, int N, int x);
void firstUpdateTmax (vector <int> * t, int N, int x);

int main() {
    int N, Q, i, j, entry, index, x, y, min, max, K;
    vector < int > tmin, tmax; //segment tree
    
    while (cin >> N) {
        K = pow(2, ceil(log(N)/log(2)));
        for (i = 0; i < 2*K; i++) {
            tmin.push_back(-1);
            tmax.push_back(-1);
        }
        for (i = 1; i <= N; i++) {
            scanf("%d", &entry);
            tmin[K-1+i] = entry;
            tmax[K-1+i] = entry;    
        }
        firstUpdateTmin(&tmin, K, 1);
        firstUpdateTmax(&tmax, K, 1);
        /*for (i = 1; i < 2*K; i++)
            cout << tmin[i] << " ";
        cout << endl;
        for (i = 1; i < 2*K; i++)
            cout << tmax[i] << " ";
        cout << endl;*/
        scanf("%d", &Q);
        for (i = 0; i < Q; i++) {
            scanf("%d", &entry);
            if (entry == 1) {
                scanf("%d", &index);
                scanf("%d", &x);
                updateTmin(&tmin, index, x, K);
                updateTmax(&tmax, index, x, K);
                /*for (j = 1; j < 2*K; j++)
                    cout << tmin[j] << " ";
                cout << endl;
                for (j = 1; j < 2*K; j++)
                    cout << tmax[j] << " ";
                cout << endl;*/
            } else {
                scanf("%d", &x);
                scanf("%d", &y);
                min = queryMin(&tmin, x, y, K, 1, 1, K);
                max = queryMax(&tmax, x, y, K, 1, 1, K);
                printf("%d\n", max - min);
            }
        }
        tmin.clear();
        tmax.clear();
    }
    return 0;
}

void updateTmin (vector < int > * t, int i, int x, int N) {
    int j = N-1+i;
    t->at(j) = x;
    do {
        j = j/2;
        if (t->at(j*2) == -1) {
            t->at(j) = t->at(j*2+1);
        } else if (t->at(j*2+1) == -1) {
            t->at(j) = t->at(j*2);
        } else {
            if (t->at(j*2) < t->at(j*2+1))
                t->at(j) = t->at(j*2);
            else
                t->at(j) = t->at(j*2+1);
        }
    } while (j > 1);
}

void updateTmax (vector < int > * t, int i, int x, int N) {
    int j = N-1+i;
    t->at(j) = x;
    do {
        j = j/2;
        if (t->at(j*2) == -1) {
            t->at(j) = t->at(j*2+1);
        } else if (t->at(j*2+1) == -1) {
            t->at(j) = t->at(j*2);
        } else {
            if (t->at(j*2) > t->at(j*2+1))
                t->at(j) = t->at(j*2);
            else
                t->at(j) = t->at(j*2+1);
        }
    } while (j > 1);
}

int queryMin (vector < int > * t, int x, int y, int N, int v, int a, int b) {
    if (a == x and b == y) {
        return t->at(v);
    } else {
        int mid = (b + a - 1)/2;
        if (y <= mid) {
            return queryMin(t, x, y, N, v*2, a, mid);
        } else if (x > mid) {
            return queryMin(t, x, y, N, v*2+1, mid+1, b);
        } else {
            int right = queryMin(t, x, mid, N, v*2, a, mid);
            int left = queryMin(t, mid+1, y, N, v*2+1, mid+1, b);
            
            if (left < right)
                return left;
            else
                return right;
        }
    }
    
    return 0;
}

int queryMax (vector < int > * t, int x, int y, int N, int v, int a, int b) {
    if (a == x and b == y) {
        return t->at(v);
    } else {
        int mid = (b + a - 1)/2;
        if (y <= mid) {
            return queryMax(t, x, y, N, v*2, a, mid);
        } else if (x > mid) {
            return queryMax(t, x, y, N, v*2+1, mid+1, b);
        } else {
            int right = queryMax(t, x, mid, N, v*2, a, mid);
            int left = queryMax(t, mid+1, y, N, v*2+1, mid+1, b);
            
            if (left > right)
                return left;
            else
                return right;
        }   
    }
    return 0;
}

void firstUpdateTmin (vector <int> * t, int N, int x) {
    if (x < N) {
        firstUpdateTmin(t, N, x*2);
        firstUpdateTmin(t, N, x*2+1);
        if (t->at(x*2) == -1) {
            t->at(x) = t->at(x*2+1);
        } else if (t->at(x*2+1) == -1) {
            t->at(x) = t->at(x*2);
        } else {
            if (t->at(x*2) < t->at(x*2+1)) {
                t->at(x) = t->at(x*2);
            } else {
                t->at(x) = t->at(x*2+1);
            }
        }
    }
}

void firstUpdateTmax (vector <int> * t, int N, int x) {
    if (x < N) {
        firstUpdateTmax(t, N, x*2);
        firstUpdateTmax(t, N, x*2+1);
        if (t->at(x*2) == -1) {
            t->at(x) = t->at(x*2+1);
        } else if (t->at(x*2+1) == -1) {
            t->at(x) = t->at(x*2);
        } else {
            if (t->at(x*2) > t->at(x*2+1)) {
                t->at(x) = t->at(x*2);
            } else {
                t->at(x) = t->at(x*2+1);
            }
        }
    }
}