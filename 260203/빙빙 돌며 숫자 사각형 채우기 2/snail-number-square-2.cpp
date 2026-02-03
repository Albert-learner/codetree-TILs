#include <bits/stdc++.h>
using namespace std;

int main() 
{
    int N, M;
    cin >> N >> M;

    vector<vector<int>> board(N, vector<int>(M, 0));

    // Please write your code here.
    int dx[4] = {1, 0, -1, 0};
    int dy[4] = {0, 1, 0, -1};

    int x = 0, y = 0;
    int num = 1;
    int dir = 0;

    for (int step = 0; step < N * M; step++) 
    {
        board[x][y] = num;

        int nx = x + dx[dir];
        int ny = y + dy[dir];

        if (nx < 0 || nx >= N || ny < 0 || ny >= M || board[nx][ny] != 0) 
        {
            dir = (dir + 1) % 4;
        }

        x += dx[dir];
        y += dy[dir];
        num++;
    }

    for (int i = 0; i < N; i++) 
    {
        for (int j = 0; j < M; j++) 
        {
            cout << board[i][j] << (j + 1 == M ? '\n' : ' ');
        }
    }
    return 0;
}