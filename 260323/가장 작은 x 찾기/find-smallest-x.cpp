#include <bits/stdc++.h>
using namespace std;

long long ceil_div(long long a, long long b) 
{
    return (a + b - 1) / b;
}

int main() 
{
    int N;
    cin >> N;

    vector<pair<long long, long long>> ab_lst(N);
    for (int i = 0; i < N; i++) 
    {
        cin >> ab_lst[i].first >> ab_lst[i].second;
    }

    vector<pair<long long, long long>> x_lst;

    for (int pair_idx = 1; pair_idx <= N; pair_idx++) 
    {
        long long a = ab_lst[pair_idx - 1].first;
        long long b = ab_lst[pair_idx - 1].second;
        long long div = 1LL << pair_idx;

        long long x_min = ceil_div(a, div);
        long long x_max = ceil_div(b, div);

        x_lst.push_back({x_min, x_max});
    }

    long long x_min_max = x_lst[0].first;
    long long x_max_min = x_lst[0].second;

    for (int i = 1; i < N; i++) 
    {
        x_min_max = max(x_min_max, x_lst[i].first);
        x_max_min = min(x_max_min, x_lst[i].second);
    }

    cout << x_min_max << '\n';
    return 0;
}