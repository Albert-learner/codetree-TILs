#include <bits/stdc++.h>
using namespace std;

int main() 
{
    vector<vector<int>> areas(2001, vector<int>(2001, 0));
    int x1, y1, x2, y2, cnts = 0;

    for(int s_idx = 0; s_idx < 3; s_idx++)
    {
        cin >> x1 >> y1 >> x2 >> y2;
        x1 += 1000; y1 += 1000;
        x2 += 1000; y2 += 1000;

        for(int r = x1; r < x2; r++)
        {
            for(int c = y1; c < y2; c++)
            {
                if(s_idx != 2)
                    areas[r][c] = 1;
                else
                    areas[r][c] = 0;
            }
        }
    }

    // Please write your code here.
    for(int r = 0; r < areas.size(); r++)
    {
        for(int c = 0; c < areas[0].size(); c++)
        {
            if(areas[r][c])
                cnts += 1;
        }
    }

    cout << cnts;
    return 0;
}