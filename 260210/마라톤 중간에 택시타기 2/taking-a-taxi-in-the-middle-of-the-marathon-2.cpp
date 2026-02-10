#include <bits/stdc++.h>
using namespace std;

static inline long long distManhattan(long long x1, long long y1, long long x2, long long y2) 
{
    return llabs(x1 - x2) + llabs(y1 - y2);
}

int main() 
{
    int N;
    cin >> N;

    vector<pair<long long, long long>> chkpnts(N);
    for (int i = 0; i < N; i++) 
    {
        cin >> chkpnts[i].first >> chkpnts[i].second;
    }

    long long total = 0;
    for (int i = 0; i < N - 1; i++) 
    {
        total += distManhattan(chkpnts[i].first, chkpnts[i].second,
                               chkpnts[i + 1].first, chkpnts[i + 1].second);
    }

    long long answer = LLONG_MAX;
    for (int i = 1; i < N - 1; i++) 
    {
        long long removed1 = distManhattan(chkpnts[i - 1].first, chkpnts[i - 1].second,
                                           chkpnts[i].first, chkpnts[i].second);
        long long removed2 = distManhattan(chkpnts[i].first, chkpnts[i].second,
                                           chkpnts[i + 1].first, chkpnts[i + 1].second);
        long long added = distManhattan(chkpnts[i - 1].first, chkpnts[i - 1].second,
                                        chkpnts[i + 1].first, chkpnts[i + 1].second);

        long long check = total - removed1 - removed2 + added;
        answer = min(answer, check);
    }

    cout << answer << "\n";
    return 0;
}