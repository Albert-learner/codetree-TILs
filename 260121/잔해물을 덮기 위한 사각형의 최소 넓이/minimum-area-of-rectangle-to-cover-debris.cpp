#include <bits/stdc++.h>
using namespace std;

int main() 
{
    static int areas[2001][2001] = {0};

    int x1, y1, x2, y2;
    int xx1, yy1, xx2, yy2;

    cin >> x1 >> y1 >> x2 >> y2;
    cin >> xx1 >> yy1 >> xx2 >> yy2;

    x1 += 1000; y1 += 1000; x2 += 1000; y2 += 1000;
    xx1 += 1000; yy1 += 1000; xx2 += 1000; yy2 += 1000;


    // Please write your code here.
    for (int i = x1; i < x2; i++) 
    {
        for (int j = y1; j < y2; j++) 
        {
            areas[i][j] = 1;
        }
    }

    for (int i = xx1; i < xx2; i++) 
    {
        for (int j = yy1; j < yy2; j++) 
        {
            areas[i][j] = 0;
        }
    }

    int min_x = 2001, min_y = 2001, max_x = 0, max_y = 0;
    for (int i = x1; i <= x2; i++) 
    {
        for (int j = y1; j <= y2; j++) 
        {
            if (areas[i][j] == 1) 
            {
                min_x = min(min_x, i);
                min_y = min(min_y, j);
                max_x = max(max_x, i);
                max_y = max(max_y, j);
            }
        }
    }
    
    if (min_x == 2001 && min_y == 2001 && max_x == 0 && max_y == 0) 
    {
        cout << 0 << "\n";
    } 
    else 
    {
        long long width = (long long)(max_x - min_x + 1);
        long long height = (long long)(max_y - min_y + 1);
        cout << width * height << "\n";
    }
    return 0;
}