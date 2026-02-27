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

    long long ans = LLONG_MAX;

    for (int i = 0; i < N; i++) 
    {
        long long minX = LLONG_MAX, maxX = LLONG_MIN;
        long long minY = LLONG_MAX, maxY = LLONG_MIN;

        for (int j = 0; j < N; j++) 
        {
            if (j == i) continue;
            minX = min(minX, x[j]);
            maxX = max(maxX, x[j]);
            minY = min(minY, y[j]);
            maxY = max(maxY, y[j]);
        }

        long long area = (maxX - minX) * (maxY - minY);
        ans = min(ans, area);
    }

    cout << ans << '\n';
    return 0;
}