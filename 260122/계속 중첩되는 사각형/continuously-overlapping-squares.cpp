#include <bits/stdc++.h>
using namespace std;


int main() 
{
    int n, x1, y1, x2, y2;
    cin >> n;
    vector<vector<char>> areas(201, vector<char>(201, 0));
    for (int r_idx = 0; r_idx < n; r_idx++) 
    {
        cin >> x1 >> y1 >> x2 >> y2;

        x1 += 100; y1 += 100; x2 += 100; y2 += 100;

        char color = (r_idx % 2 == 0) ? 'R' : 'B';

        for (int i = x1; i < x2; i++) 
        {
            for (int j = y1; j < y2; j++) 
            {
                areas[i][j] = color;
            }
        }
    }

    // Please write your code here.
    int blue_cnts = 0;
    for (int i = 0; i < 201; i++) 
    {
        for (int j = 0; j < 201; j++) 
        {
            if (areas[i][j] == 'B') blue_cnts++;
        }
    }

    cout << blue_cnts << "\n";
    return 0;
}