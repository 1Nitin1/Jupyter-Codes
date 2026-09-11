#include <bits/stdc++.h>
using namespace std;

struct Node {
    int val;
    int index;
    Node(int v, int i) : val(v), index(i) {}
};

deque<Node> dq;

int modded(int a, int b, int c, int x) {
    long long ans = ( (1LL * a % c) * (x % c) ) % c;
    ans = (ans + (1LL * b % c)) % c;
    return (int)ans;
}

void push(int a, int index) {
    while (!dq.empty() && dq.back().val >= a) {
        dq.pop_back();
    }
    dq.emplace_back(a, index);
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, k;
    cin >> n >> k;
    int x, a, b, c;
    cin >> x >> a >> b >> c;

    int y = x;
    long long xr = 0;

    // First k elements
    for (int i = 0; i < k; i++) {
        push(x, i);
        x = modded(a, b, c, x);
    }
    xr ^= dq.front().val;

    // Remaining elements
    for (int i = k; i < n; i++) {
        if (dq.front().index == i - k) {
            dq.pop_front();
        }
        y = modded(a, b, c, y);
        push(x, i);
        x = modded(a, b, c, x);
        xr ^= dq.front().val;
    }

    cout << xr << "\n";
    return 0;
}
