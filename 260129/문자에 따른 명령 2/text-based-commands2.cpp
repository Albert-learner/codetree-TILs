#include <bits/stdc++.h>
using namespace std;

int main() 
{
    string moves;
    cin >> moves;

    // Please write your code here.
    long long x = 0, y = 0;
    int dir_num = 3;
    int dx[4] = {1, 0, -1, 0};
    int dy[4] = {0, -1, 0, 1};

    for(char move: moves)
    {
        if(move == 'L')
            dir_num = (dir_num - 1 + 4) % 4;
        else if(move == 'R')
            dir_num = (dir_num + 1) % 4;
        else
        {
            x += dx[dir_num];
            y += dy[dir_num];
        }
    }

    cout << x << ' ' << y << endl;
    
    return 0;
}