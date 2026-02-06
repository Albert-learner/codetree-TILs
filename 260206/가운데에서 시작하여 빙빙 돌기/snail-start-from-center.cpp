#include <bits/stdc++.h>
using namespace std;

int main() 
{
    int N;
    cin >> N;

    vector<vector<long long>> board(N, vector<long long>(N, 0));

    int x = N - 1, y = N - 1;
    int dx[4] = {0, -1, 0, 1};
    int dy[4] = {-1, 0, 1, 0};
    int dir = 0;

    long long num = 1LL * N * N;

    for (long long step = 0; step < 1LL * N * N; step++) 
    {
        board[x][y] = num;

        int nx = x + dx[dir];
        int ny = y + dy[dir];

        if (nx < 0 || nx >= N || ny < 0 || ny >= N || board[nx][ny] != 0) 
        {
            dir = (dir + 1) % 4;
            nx = x + dx[dir];
            ny = y + dy[dir];
        }

        x = nx;
        y = ny;
        num--;
    }

    for (int i = 0; i < N; i++) 
    {
        for (int j = 0; j < N; j++) 
        {
            cout << board[i][j] << (j + 1 == N ? '\n' : ' ');
        }
    }
    return 0;
}
