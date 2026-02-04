#include <bits/stdc++.h>
using namespace std;

int n, m;

int main() 
{
    int N, M;
    cin >> N >> M;

    vector<vector<char>> board(N, vector<char>(M, 0));

    // Please write your code here.
    int x = 0, y = 0;
    char move_chr = 'A';
    int dx[4] = {0, 1, 0, -1};
    int dy[4] = {1, 0, -1, 0};
    int dir_num = 0;

    for (int step = 0; step < N * M; step++) 
    {
        board[x][y] = move_chr;

        int mx = x + dx[dir_num];
        int my = y + dy[dir_num];

        if (mx < 0 || mx >= N || my < 0 || my >= M || board[mx][my] != 0) 
        {
            dir_num = (dir_num + 1) % 4;
            mx = x + dx[dir_num];
            my = y + dy[dir_num];
        }

        x = mx;
        y = my;

        move_chr = (move_chr == 'Z') ? 'A' : char(move_chr + 1);
    }

    for (int i = 0; i < N; i++) 
    {
        for (int j = 0; j < M; j++) 
        {
            cout << board[i][j];
            if (j + 1 < M) cout << ' ';
        }
        cout << '\n';
    }
    return 0;
}
