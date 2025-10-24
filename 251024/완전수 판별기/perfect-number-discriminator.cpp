#include <bits/stdc++.h>
using namespace std;

int main() {
    long long N;
    if (!(cin >> N)) return 0;

    long long sumDiv = 0;
    for (long long i = 1; i * i <= N; ++i) {
        if (N % i == 0) {
            sumDiv += i;

            long long other = N / i;
            if (other != i && other != N) {
                sumDiv += other;
            }
        }
    }

    if (sumDiv == N) cout << 'P';
    else cout << 'N';

    return 0;
}
