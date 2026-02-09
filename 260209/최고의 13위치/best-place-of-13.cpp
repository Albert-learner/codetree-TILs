#include <bits/stdc++.h>
using namespace std;

int main() 
{
    int N;
    cin >> N;

    vector<vector<int>> board(N, vector<int>(N));
    for (int i = 0; i < N; i++)
        for (int j = 0; j < N; j++) cin >> board[i][j];

    // Please write your code here.
    int max_cnts = 0;
    for(int i = 0; i < N; i++)
    {
        for(int j = 0; j < N - 2; j++)
        {
            max_cnts = max(max_cnts, board[i][j] + board[i][j + 1] + board[i][j + 2]);
        }
    }

    cout << max_cnts;
    return 0;
}