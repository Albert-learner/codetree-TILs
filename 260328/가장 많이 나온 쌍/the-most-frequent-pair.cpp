#include <bits/stdc++.h>
using namespace std;

int main() 
{
    int N, M;
    cin >> N >> M;

    map<pair<int, int>, int> pairs_dict;
    for (int i = 0; i < M; i++) 
    {
        int a, b;
        cin >> a >> b;

        if (a > b) swap(a, b);
        pairs_dict[{a, b}]++;
    }

    // Please write your code here.
    int max_val = 0;
    for (const auto& p : pairs_dict) 
    {
        max_val = max(max_val, p.second);
    }

    cout << max_val << '\n';
    return 0;
}
