#include <bits/stdc++.h>
using namespace std;

int main() 
{
    int N;
    cin >> N;

    vector<pair<long long, long long>> lines(N);
    for (int i = 0; i < N; i++) 
    {
        long long a, b;
        cin >> a >> b;
        lines[i] = {a, b};
    }

    // Please write your code here.
    auto check_cross = [&](int num) -> bool 
    {
        int some = 0;

        long long p0 = lines[num].first;
        long long p1 = lines[num].second;
        long long p_diff = p1 - p0;

        for (int p = 0; p < N; p++) 
        {
            if (p == num) continue;

            long long cp0 = lines[p].first;
            long long cp1 = lines[p].second;
            long long cp_diff = cp1 - cp0;

            long long up = p0 * cp_diff - cp0 * p_diff;
            long long down = cp_diff - p_diff;

            if (down != 0) 
            {
                long double result = (long double)up / (long double)down;

                long double pmin = (long double)min(p0, p1);
                long double pmax = (long double)max(p0, p1);
                long double cpmin = (long double)min(cp0, cp1);
                long double cpmax = (long double)max(cp0, cp1);

                if (pmin <= result && result <= pmax &&
                    cpmin <= result && result <= cpmax) 
                {
                    some += 1;
                }
            }
        }

        return (some == 0);
    };

    int cnts = 0;
    for (int i = 0; i < N; i++) {
        if (check_cross(i)) cnts++;
    }

    cout << cnts << "\n";
    return 0;
}