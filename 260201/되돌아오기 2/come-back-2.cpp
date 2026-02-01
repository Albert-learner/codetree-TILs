#include <bits/stdc++.h>
using namespace std;

int main() 
{
    string moves;
    cin >> moves;

    // Please write your code here.
    int dir_num = 0;
    int dx[4] = {0, 1, 0, -1};
    int dy[4] = {1, 0, -1, 0};

    long long x = 0, y = 0;
    vector<pair<long long, long long>> coords;

    long long answer = 0;
    long long times = 0;

    for (char mv : moves) 
    {
        if (mv == 'L') 
        {
            dir_num = (dir_num + 3) % 4;
        } 
        else if (mv == 'R') 
        {
            dir_num = (dir_num + 1) % 4;
        } 
        else 
        {
            x += dx[dir_num];
            y += dy[dir_num];

            if (x == 0 && y == 0) 
            {
                times += 1;
                answer += times;
                coords.push_back({x, y});
                break;
            }
            coords.push_back({x, y});
        }

        if (x == 0 && y == 0) break;
        times += 1;
    }

    bool hasOrigin = false;
    for (auto &p : coords) 
    {
        if (p.first == 0 && p.second == 0) 
        {
            hasOrigin = true;
            break;
        }
    }
    if (!hasOrigin) answer = -1;

    cout << answer << "\n";
    return 0;
}