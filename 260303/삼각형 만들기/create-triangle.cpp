#include <bits/stdc++.h>
using namespace std;

using ll = long long;

static inline bool is_parallel(const pair<ll,ll>& p1,
                               const pair<ll,ll>& p2,
                               const pair<ll,ll>& p3) 
{
    ll x1 = p1.first,  y1 = p1.second;
    ll x2 = p2.first,  y2 = p2.second;
    ll x3 = p3.first,  y3 = p3.second;

    // Same logic as Python:
    // (any two share x) AND (any two share y)
    bool hasSameX = (x1 == x2) || (x2 == x3) || (x3 == x1);
    bool hasSameY = (y1 == y2) || (y2 == y3) || (y3 == y1);
    return hasSameX && hasSameY;
}

int main() 
{
    int N;
    cin >> N;
    vector<pair<ll,ll>> coords(N);
    for (int i = 0; i < N; i++) 
    {
        cin >> coords[i].first >> coords[i].second;
    }

    // Please write your code here.
    ll max_areas = 0;

    for (int i = 0; i < N; i++) 
    {
        for (int j = i + 1; j < N; j++) 
        {
            for (int k = j + 1; k < N; k++) 
            {
                const auto& first  = coords[i];
                const auto& second = coords[j];
                const auto& third  = coords[k];

                if (is_parallel(first, second, third)) 
                {
                    ll x1 = first.first,  y1 = first.second;
                    ll x2 = second.first, y2 = second.second;
                    ll x3 = third.first,  y3 = third.second;

                    ll x_min = min({x1, x2, x3});
                    ll x_max = max({x1, x2, x3});
                    ll y_min = min({y1, y2, y3});
                    ll y_max = max({y1, y2, y3});

                    ll diff = (x_max - x_min) * (y_max - y_min);
                    max_areas = max(max_areas, diff);
                }
            }
        }
    }

    cout << max_areas << "\n";
    return 0;
}