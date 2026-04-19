#include <bits/stdc++.h>
using namespace std;

int main() 
{
    int N;
    cin >> N;
    vector<long long> x(N), y(N);
    for (int i = 0; i < N; i++) 
    {
        cin >> x[i] >> y[i];
    }

    // Please write your code here.
    long long ans = LLONG_MAX;

    for (int i = 0; i < N; i++) 
    {
        for (int j = i + 1; j < N; j++) 
        {
            long long dx = x[i] - x[j];
            long long dy = y[i] - y[j];
            long long dist2 = dx * dx + dy * dy;
            ans = min(ans, dist2);
        }
    }

    cout << ans << '\n';
    return 0;
}