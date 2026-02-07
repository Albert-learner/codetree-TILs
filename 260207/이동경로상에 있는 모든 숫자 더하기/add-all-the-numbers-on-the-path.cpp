#include <bits/stdc++.h>
using namespace std;

int main() 
{
    int N, T;
    cin >> N >> T;

    string commands;
    cin >> commands;

    vector<vector<long long>> board(N, vector<long long>(N));
    for (int i = 0; i < N; i++) 
    {
        for (int j = 0; j < N; j++) cin >> board[i][j];
    }

    int dx[4] = {-1, 0, 1, 0};
    int dy[4] = {0, 1, 0, -1};

    int x = N / 2, y = N / 2;
    int dir = 0;

    long long answer = board[x][y];

    for (char cmd : commands) 
    {
        if (cmd == 'R') 
        {
            dir = (dir + 1) % 4;
        } 
        else if (cmd == 'L') 
        {
            dir = (dir + 3) % 4;
        } else 
        {
            int nx = x + dx[dir];
            int ny = y + dy[dir];
            if (0 <= nx && nx < N && 0 <= ny && ny < N) 
            {
                x = nx; y = ny;
                answer += board[x][y];
            }
        }
    }

    cout << answer << "\n";
    return 0;
}