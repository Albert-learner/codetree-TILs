#include <bits/stdc++.h>
using namespace std;

static bool noCarry(long long x, long long y, long long z) 
{
    while (x > 0 || y > 0 || z > 0) {
        if ((x % 10) + (y % 10) + (z % 10) > 9) return false;
        x /= 10;
        y /= 10;
        z /= 10;
    }
    return true;
}

int main() 
{
    int N;
    cin >> N;
    vector<long long> a(N);
    for (int i = 0; i < N; i++) 
    {
        cin >> a[i];
    }

    // Please write your code here.
    long long ans = -1;

    for (int i = 0; i < N; i++) 
    {
        for (int j = i + 1; j < N; j++) 
        {
            for (int k = j + 1; k < N; k++) 
            {
                if (noCarry(a[i], a[j], a[k])) 
                {
                    ans = max(ans, a[i] + a[j] + a[k]);
                }
            }
        }
    }

    cout << ans << "\n";
    return 0;
}
