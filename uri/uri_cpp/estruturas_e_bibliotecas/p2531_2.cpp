#include <iostream>
#include <sstream>
#include <string>
#include <stdlib.h>
#include <stdio.h>
#include <vector>

using namespace std;

vector <int> update (vector < int > t, int i, int x, int N);
int query (vector < int > t, int x, int y, int N, int v, int a, int b);
vector <int> firstUpdate (vector <int> t, int N, int x);

int main() {
    int N, Q, i, j, entry, index, x, y, min, max;
    vector < pair <int, int> > t; //segment tree
    
    while (cin >> N) {
        for (i = 0; i < 2*N; i++) {
            pair <int, int> p;
            p.first = -1;
            p.second = -1;
            t.push_back(p);
        }
        for (i = 1; i <= N; i++) {
            scanf("%d", &entry);
            t[N-1+i].first = entry;
            t[N-1+i].second = entry;
        }
        t 
        /*for (i = 1; i < 2*N; i++)
            cout << tmin[i] << " ";
        cout << endl;*/
        scanf("%d", &Q);
        for (i = 0; i < Q; i++) {
            scanf("%d", &entry);
            if (entry == 1) {
                scanf("%d", &index);
                scanf("%d", &x);
                tmin = updateTmin(tmin, index, x, N);
                tmax = updateTmax(tmax, index, x, N);
            } else {
                scanf("%d", &x);
                scanf("%d", &y);
                min = queryMin(tmin, x, y, N, 1, 1, N);
                max = queryMax(tmax, x, y, N, 1, 1, N);
                printf("%d\n", max - min);
            }
        }
        tmin.clear();
        tmax.clear();
    }
    return 0;
}

vector <int> updateTmin (vector < int > t, int i, int x, int N) {
    int j = N-1+i;
    t[j] = x;
    do {
        j = j/2;
        if (t[j*2] == -1) {
            t[j] = t[j*2+1];
        } else if (t[j*2+1] == -1) {
            t[j] = t[j*2];
        } else {
            if (t[j*2] < t[j*2+1])
                t[j] = t[j*2];
            else
                t[j] = t[j*2+1];
        }
    } while (j > 1);
    return t;
}

vector <int> updateTmax (vector < int > t, int i, int x, int N) {
    int j = N-1+i;
    t[j] = x;
    do {
        j = (j-1)/2;
        if (t[j*2] == -1) {
            t[j] = t[j*2+1];
        } else if (t[j*2+1] == -1) {
            t[j] = t[j*2];
        } else {
            if (t[j*2] > t[j*2+1])
                t[j] = t[j*2];
            else
                t[j] = t[j*2+1];
        }
    } while (j > 0);
    return t;
}

int queryMin (vector < int > t, int x, int y, int N, int v, int a, int b) {
    if (a == x and b == y) {
        return t[v];
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

int queryMax (vector < int > t, int x, int y, int N, int v, int a, int b) {
    if (a == x and b == y) {
        return t[v];
    } else {
        int mid = (b + a - 1)/2;
        if (y <= mid) {
            return queryMin(t, x, y, N, v*2, a, mid);
        } else if (x > mid) {
            return queryMin(t, x, y, N, v*2+1, mid+1, b);
        } else {
            int right = queryMin(t, x, mid, N, v*2, a, mid);
            int left = queryMin(t, mid+1, y, N, v*2+1, mid+1, b);
            
            if (left > right)
                return left;
            else
                return right;
        }   
    }
    return 0;
}

vector <int> firstUpdateTmin (vector <int> t, int N, int x) {
    if (x >= N) {
        return t;
    } else {
        t = firstUpdateTmin(t, N, x*2);
        t = firstUpdateTmin(t, N, x*2+1);
        if (t[x*2] < t[x*2+1]) {
            t[x] = t[x*2];
        } else {
            t[x] = t[x*2+1];
        }
        return t;
    }
}

vector <int> firstUpdateTmax (vector <int> t, int N, int x) {
    if (x >= N) {
        return t;
    } else {
        t = firstUpdateTmax(t, N, x*2);
        t = firstUpdateTmax(t, N, x*2+1);
        if (t[x*2] > t[x*2+1]) {
            t[x] = t[x*2];
        } else {
            t[x] = t[x*2+1];
        }
        return t;
    }
}