// Segment tree lazy propagation sum
#include <iostream>
#include <sstream>
#include <string>
#include <stdlib.h>
#include <stdio.h>
#include <vector>
#include <math.h>

using namespace std;

void changeInterval (vector < long long > * tree, vector < long long > * update, int x, int p, int q, long long v, int K, int a, int b);
long long query (vector < long long > * tree, vector < long long > * update, int x, int p, int q, int K, int a, int b);

int main() {
    int N, Q, i, j, entry, index, p, q, K, t, T, c;
    long long v, r;
    vector < long long > tree; //segment tree
    vector < long long > update; // array pending update - just for intern nodes
    
    cin >> T;
    for (t = 0; t < T; t++) {
        scanf("%d", &N);
        scanf("%d", &Q);
        K = pow(2, ceil(log(N)/log(2)));
        for (i = 0; i < 2*K; i++)
            tree.push_back(0);
        for (i = 0; i < 2*K; i++)
            update.push_back(0);
        
        for (i = 0; i < Q; i++) {
            scanf("%d", &c);
            if (c == 0) {
                scanf("%d", &p);
                scanf("%d", &q);
                scanf("%lld", &v);
                changeInterval(&tree, &update, 1, p, q, v, 2*K, 1, K);
            } else {
                scanf("%d", &p);
                scanf("%d", &q);
                r = query(&tree, &update, 1, p, q, 2*K, 1, K);
                printf("%lld\n", r);
            }
            /*cout << "t: ";
            for (j = 1; j < 2*K; j++)
                cout << tree[j] << " ";
            cout << endl;
            cout << "u: ";
            for (j = 1; j < 2*K; j++)
                cout << update[j] << " ";
            cout << endl << endl;*/
        }
        tree.clear();
        update.clear();
    }
    return 0;
}

void changeInterval (vector < long long > * tree, vector < long long > * update, int x, int p, int q, long long v, int K, int a, int b) {
    if (a == p and b == q) {
        update->at(x) += (v*(q-p+1));
    } else {
        tree->at(x) += (v*(q-p+1));
        int mid = (b + a - 1)/2;
        if (q <= mid) {
            changeInterval(tree, update, x*2, p, q, v, K, a, mid);
        } else if (p > mid) {
            changeInterval(tree, update, x*2+1, p, q, v, K, mid+1, b);
        } else {
            changeInterval(tree, update, x*2, p, mid, v, K, a, mid);
            changeInterval(tree, update, x*2+1, mid+1, q, v, K, mid+1, b);
        }
    }
}

long long query (vector < long long > * tree, vector < long long > * update, int x, int p, int q, int K, int a, int b) {
    tree->at(x) += update->at(x);
    if (x < K/2) {
        update->at(x*2) += (update->at(x)/2);
        update->at(x*2+1) += (update->at(x)/2);
    }
    update->at(x) = 0;
    if (a == p and b == q) {
        return tree->at(x);
    } else {
        int mid = (b + a - 1)/2;
        if (q <= mid) {
            return query(tree, update, x*2, p, q, K, a, mid);
        } else if (p > mid) {
            return query(tree, update, x*2+1, p, q, K, mid+1, b);
        } else {
            long right = query(tree, update, x*2, p, mid, K, a, mid);
            long left = query(tree, update, x*2+1, mid+1, q, K, mid+1, b);
            return right+left;
        }
    }
}