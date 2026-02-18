#include <iostream>

using namespace std;


int main() 
{
    int N;
    long long S;
    cin >> N >> S;
    vector<long long> n_lst(N);
    for (int i = 0; i < N; i++) cin >> n_lst[i];

    vector<long long> sums;
    sums.reserve(1LL * N * (N - 1) / 2);

    for (int i = 0; i < N; i++) {
        for (int j = i + 1; j < N; j++) {
            long long total = 0;
            for (int k = 0; k < N; k++) {
                if (k == i || k == j) continue;
                total += n_lst[k];
            }
            sums.push_back(total);
        }
    }

    sort(sums.begin(), sums.end(), [&](long long a, long long b) {
        return llabs(S - a) < llabs(S - b);
    });

    cout << llabs(sums[0] - S) << "\n";
    return 0;
}