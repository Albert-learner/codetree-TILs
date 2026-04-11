#include <bits/stdc++.h>
using namespace std;


int main() 
{
    int K, N;
    cin >> K >> N;

    const int MAX_N = 20;
    vector<vector<int>> win_cnts(MAX_N + 1, vector<int>(MAX_N + 1, 0));

    int answer = 0;

    for (int g = 0; g < K; g++) 
    {
        vector<int> game(N);
        for (int i = 0; i < N; i++) 
        {
            cin >> game[i];
        }

        for (int i = 0; i < N; i++) 
        {
            for (int j = i + 1; j < N; j++) 
            {
                win_cnts[game[i]][game[j]] += 1;
            }
        }
    }

    for (int i = 1; i <= N; i++) 
    {
        for (int j = 1; j <= N; j++) 
        {
            if (win_cnts[i][j] == K) 
            {
                answer += 1;
            }
        }
    }

    cout << answer << '\n';
    return 0;
}