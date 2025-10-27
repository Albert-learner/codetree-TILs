#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long a, b;
    if (!(cin >> a >> b)) return 0;

    long long g = gcd(1920LL, 2880LL); // 공약수들은 gcd의 약수들

    bool ok = false;
    for (long long i = 1; i * i <= g; ++i) {
        if (g % i == 0) {
            long long d1 = i;
            long long d2 = g / i;
            if ((a <= d1 && d1 <= b) || (a <= d2 && d2 <= b)) {
                ok = true;
                break;
            }
        }
    }

    cout << (ok ? 1 : 0) << '\n';
    return 0;
}
