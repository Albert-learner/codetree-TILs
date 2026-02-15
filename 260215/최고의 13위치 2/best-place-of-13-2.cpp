#include <bits/stdc++.h>
using namespace std;

int main() 
{
    int N;
    cin >> N;
    vector<vector<int>> grid(N, vector<int>(N));
    for (int i = 0; i < N; i++) 
    {
        for (int j = 0; j < N; j++) cin >> grid[i][j];
    }

    int answer = 0;

    for (int i = 0; i < N; i++) 
    {
        for (int j = 0; j <= N - 3; j++) 
        {
            for (int k = 0; k < N; k++) 
            {
                for (int l = 0; l <= N - 3; l++) 
                {

                    if (i == k && abs(l - j) <= 2) continue;

                    int cnt1 = grid[i][j] + grid[i][j + 1] + grid[i][j + 2];
                    int cnt2 = grid[k][l] + grid[k][l + 1] + grid[k][l + 2];
                    answer = max(answer, cnt1 + cnt2);
                }
            }
        }
    }

    cout << answer << "\n";
    return 0;
}
