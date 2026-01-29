#include <bits/stdc++.h>
using namespace std;

int main() 
{
    int N;
    cin >> N;

    vector<vector<int>> board(N, vector<int>(N));
    for (int i = 0; i < N; i++) 
    {
        for (int j = 0; j < N; j++) cin >> board[i][j];
    }

    // up, down, left, right
    int dx[4] = {-1, 1, 0, 0};
    int dy[4] = {0, 0, -1, 1};

    int answer = 0;

    for (int i = 0; i < N; i++) 
    {
        for (int j = 0; j < N; j++) 
        {
            int cnts = 0;
            for (int dir = 0; dir < 4; dir++) 
            {
                int nx = i + dx[dir];
                int ny = j + dy[dir];
                if (0 <= nx && nx < N && 0 <= ny && ny < N) 
                {
                    if (board[nx][ny] == 1) cnts++;
                }
            }
            if (cnts >= 3) answer++;
        }
    }

    cout << answer << "\n";
    return 0;
}