#include <bits/stdc++.h>
using namespace std;


int main() 
{
    int N, x, y;
    cin >> N;

    vector<pair<int,int>> squares(N);
    for (int i = 0; i < N; i++) 
    {
        cin >> x >> y;
        x += 100;
        y += 100;
        squares[i] = {x, y};
    }
    vector<vector<int>> areas(201, vector<int>(201, 0));

    // Please write your code here.
    for (auto [x, y] : squares) 
    {
        for (int row = x; row < x + 8; row++) 
        {
            for (int col = y; col < y + 8; col++) 
            {
                areas[row][col] = 1;
            }
        }
    }

    int cnts = 0;
    for (int row = 0; row < 201; row++) 
    {
        for (int col = 0; col < 201; col++) 
        {
            if (areas[row][col] == 1) cnts++;
        }
    }

    cout << cnts << "\n";
    return 0;
}
