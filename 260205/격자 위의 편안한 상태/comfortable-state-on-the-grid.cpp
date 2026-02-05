#include <bits/stdc++.h>
using namespace std;

int main() 
{
    int N, M, r, c;
    cin >> N >> M;
    vector<vector<int>> board(N, vector<int>(N, 0));
    const int dr[4] = {-1, 1, 0, 0};
    const int dc[4] = {0, 0, -1, 1};

    for (int i = 0; i < M; i++) 
    {
        cin >> r >> c;
        r -= 1; c -= 1;
        board[r][c] = 1;

        int colors = 0;
        for(int k = 0; k < 4; k++)
        {
            int mr = r + dr[k];
            int mc = c + dc[k];
            if(0 <= mr && mr < N && 0 <= mc && mc < N && board[mr][mc] == 1)
                colors += 1;
        }

        cout << (colors == 3 ? 1 : 0) << endl;
    }
    return 0;
}
