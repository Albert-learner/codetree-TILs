#include <bits/stdc++.h>
using namespace std;

int main() 
{
    const int MAX_H = 100;
    const int K = 17;
    const long long INT_MAX_LL = LLONG_MAX;

    int n;
    cin >> n;

    vector<int> arr(n);
    for (int i = 0; i < n; i++) 
    {
        cin >> arr[i];
    }

    long long ans = INT_MAX_LL;

    for (int i = 0; i < MAX_H; i++) 
    {
        long long cost = 0;

        for (int j = 0; j < n; j++) 
        {
            if (arr[j] < i) 
            {
                long long diff = arr[j] - i;
                cost += diff * diff;
            }
            if (arr[j] > i + K) 
            {
                long long diff = arr[j] - i - K;
                cost += diff * diff;
            }
        }

        ans = min(ans, cost);
    }

    cout << ans << '\n';
    return 0;
}