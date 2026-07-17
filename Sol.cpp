#include <bits/stdc++.h>
using namespace std;

long long query(const vector<int>& arr, const vector<long long>& block, int l, int r, int sn) {
    long long min_val = LLONG_MAX;
    if (l / sn == r / sn) {
        for (int i = l; i <= r; i++) {
            min_val = min(min_val, (long long) arr[i]);
        }
    } else {
        for (int i = l; i < (l / sn + 1) * sn; i++) {
            min_val = min(min_val, (long long) arr[i]);
        }
        for (int i = l / sn + 1; i < r / sn; i++) {
            min_val = min(min_val, block[i]);
        }
        for (int i = (r / sn) * sn; i <= r; i++) {
            min_val = min(min_val, (long long) arr[i]);
        }
    }
    return min_val;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, q;
    cin >> n >> q;
    vector<int> arr(n);
    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }

    int sn = (int) sqrt(n);
    sn = (n + sn - 1) / sn;  // number of blocks
    vector<long long> block(sn, LLONG_MAX);

    for (int i = 0; i < n; i++) {
        block[i / sn] = min(block[i / sn], (long long) arr[i]);
    }

    while (q--) {
        int u, v;
        cin >> u >> v;
        cout << query(arr, block, u - 1, v - 1, sn) << "\n";
    }

    return 0;
}
