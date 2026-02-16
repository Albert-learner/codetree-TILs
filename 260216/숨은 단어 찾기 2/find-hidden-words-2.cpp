#include <bits/stdc++.h>
using namespace std;

int main() 
{
    int N, M;
    cin >> N >> M;

    vector<string> board(N);
    for (int i = 0; i < N; i++) cin >> board[i];

    int dr[8] = {-1, -1, -1,  0,  1, 1,  1,  0};
    int dc[8] = {-1,  0,  1,  1,  1, 0, -1, -1};

    long long answer = 0;

    for (int i = 0; i < N; i++) 
    {
        for (int j = 0; j < M; j++) 
        {
            for (int k = 0; k < 8; k++) 
            {
                int ni2 = i + 2 * dr[k];
                int nj2 = j + 2 * dc[k];

                if (0 <= ni2 && ni2 < N && 0 <= nj2 && nj2 < M) 
                {
                    int ni1 = i + dr[k];
                    int nj1 = j + dc[k];

                    if (board[i][j] == 'L' &&
                        board[ni1][nj1] == 'E' &&
                        board[ni2][nj2] == 'E')
                    {
                        answer++;
                    }
                }
            }
        }
    }

    cout << answer << "\n";
    return 0;
}
