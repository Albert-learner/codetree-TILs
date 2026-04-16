#include <bits/stdc++.h>
using namespace std;

int main() 
{
    // Please write your code here.
    int N;
    cin >> N;
    vector<pair<int, int>> games(N);
    for(int i = 0; i < N; i++)
        cin >> games[i].first >> games[i].second;

    int max_wins = 0, wins = 0;
    for(auto [a, b]: games)
    {
        if(a == 1 && b == 2)
            wins += 1;
        else if(a == 2 && b == 3)
            wins += 1;
        else if(a == 3 && b == 1)
            wins += 1;
    }

    max_wins = max(max_wins, wins);
    wins = 0;
    for(auto [a, b]: games)
    {
        if(a == 1 && b == 3)
            wins += 1;
        else if(a == 3 && b == 2)
            wins += 1;
        else if(a == 2 && b == 1)
            wins += 1;
    }

    max_wins = max(max_wins, wins);
    cout << max_wins;
    return 0;
}

