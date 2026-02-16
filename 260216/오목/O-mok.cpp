#include <bits/stdc++.h>
using namespace std;

int board[19][19];

int winner = 0;
pair<int,int> mid_coord = {-1, -1};

int dx[4] = {-1, -1, 0, 1};
int dy[4] = { 0,  1, 1, 1};

void DFS(int x, int y, int cnt, int color, int f_dir) 
{
    if (winner != 0) return; 

    if (cnt == 5) 
    {
        winner = color;
        mid_coord = {x - dx[f_dir] * 2, y - dy[f_dir] * 2};
        return;
    }

    int mx = x + dx[f_dir];
    int my = y + dy[f_dir];

    if (0 <= mx && mx < 19 && 0 <= my && my < 19 && board[mx][my] == color) 
    {
        DFS(mx, my, cnt + 1, color, f_dir);
    } 
    else 
    {
        return;
    }
}

int main()
{
    for (int i = 0; i < 19; i++) 
    {
        for (int j = 0; j < 19; j++) 
        {
            cin >> board[i][j];
        }
    }

    for (int i = 0; i < 19; i++) 
    {
        for (int j = 0; j < 19; j++) 
        {
            if (board[i][j] == 1 || board[i][j] == 2) 
            {
                for (int k = 0; k < 4; k++) 
                {
                    DFS(i, j, 1, board[i][j], k);
                }
            }
        }
    }

    if (winner != 0) 
    {
        cout << winner << "\n";
        cout << mid_coord.first + 1 << " " << mid_coord.second + 1 << "\n";
    } 
    else
    {
        cout << 0 << "\n";
    }

    return 0;
}
