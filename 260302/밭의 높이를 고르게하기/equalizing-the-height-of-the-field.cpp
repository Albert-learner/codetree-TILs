#include <bits/stdc++.h>
using namespace std;

int main() 
{
    int N, H, T;
    cin >> N >> H >> T;

    vector<int> heights(N);
    for (int i = 0; i < N; i++) cin >> heights[i];

    // Please write your code here.
    const int INF = 100000;
    int min_cost = INF;

    for (int i = 0; i + T <= N; i++) 
    {
        long long cost = 0;
        for (int j = i; j < i + T; j++) 
        {
            cost += llabs((long long)heights[j] - H); 
        }
        min_cost = min<long long>(min_cost, cost);
    }

    cout << min_cost << "\n";
    return 0;
}