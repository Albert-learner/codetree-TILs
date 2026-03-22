#include <bits/stdc++.h>
using namespace std;

int main() 
{
    int N;
    cin >> N;

    vector<vector<int>> turnovers(N, vector<int>(3));
    for (int i = 0; i < N; i++) 
    {
        cin >> turnovers[i][0] >> turnovers[i][1] >> turnovers[i][2];
    }

    int max_cnts = 0;

    for (int stone = 1; stone <= 3; stone++) 
    {
        vector<int> maps(4, 0);
        int cnts = 0;
        maps[stone] = 1;

        for (int j = 0; j < N; j++) 
        {
            // Same swap as Python code
            swap(turnovers[j][0], turnovers[j][1]);

            swap(maps[turnovers[j][0]], maps[turnovers[j][1]]);

            if (maps[turnovers[j][2]] == 1) 
            {
                cnts += 1;
            }
        }

        max_cnts = max(max_cnts, cnts);
    }

    cout << max_cnts << '\n';
    return 0;
}
