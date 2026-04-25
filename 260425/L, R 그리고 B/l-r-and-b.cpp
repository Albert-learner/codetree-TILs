#include <bits/stdc++.h>
using namespace std;

class Push
{
    public:
        int r, c;
        Push(int row, int col)
        {
            r = row;
            c = col;
        }
};

bool index_ok(int r, int c)
{
    return 0 <= r && r < 10 && 0 <= c && c < 10;
}

vector<vector<char>> arr(10, vector<char>(10));
vector<vector<int>> dp(10, vector<int>(10, 0));
queue<Push> q;

void bfs() 
{
    int dr[4] = {-1, 1, 0, 0};
    int dc[4] = {0, 0, -1, 1};

    while (!q.empty()) 
    {
        Push p = q.front();
        q.pop();

        for (int i = 0; i < 4; i++) 
        {
            int next_r = p.r + dr[i];
            int next_c = p.c + dc[i];

            if (index_ok(next_r, next_c) && arr[next_r][next_c] != 'R' && dp[next_r][next_c] == 0) 
            {
                dp[next_r][next_c] = dp[p.r][p.c] + 1;
                Push p2(next_r, next_c);
                q.push(p2);
            }
        }
    }
}

int main() 
{
    // Please write your code here.
    int str_i = -1, str_j = -1;
    int las_i = -1, las_j = -1;

    for (int i = 0; i < 10; i++) 
    {
        string row;
        cin >> row;
        for (int j = 0; j < 10; j++) 
        {
            arr[i][j] = row[j];
            if (arr[i][j] == 'B' || arr[i][j] == 'L') 
            {
                if (str_i != -1) 
                {
                    las_i = i;
                    las_j = j;
                } 
                else 
                {
                    str_i = i;
                    str_j = j;
                }
            }
        }
    }

    Push p(str_i, str_j);
    q.push(p);
    bfs();

    cout << dp[las_i][las_j] - 1 << '\n';

    return 0;
}
