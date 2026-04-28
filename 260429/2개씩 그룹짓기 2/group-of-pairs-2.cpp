#include <bits/stdc++.h>
using namespace std;

int main() 
{
    // Please write your code here.
    int N;
    cin >> N;
    vector<int> n_lst(2 * N);
    for (int i = 0; i < 2 * N; i++) 
    {
        cin >> n_lst[i];
    }

    sort(n_lst.begin(), n_lst.end());

    vector<pair<int, int>> bundles;
    for (int i = 0; i < N; i++) 
    {
        bundles.push_back({n_lst[i], n_lst[i + N]});
    }

    sort(bundles.begin(), bundles.end(), [](const pair<int, int>& a, const pair<int, int>& b) 
    {
        return abs(a.first - a.second) < abs(b.first - b.second);
    });

    cout << abs(bundles[0].first - bundles[0].second) << '\n';

    return 0;
}