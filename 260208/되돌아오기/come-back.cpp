#include <bits/stdc++.h>
using namespace std;

int main() 
{
    int N;
    cin >> N;

    unordered_map<char, pair<int,int>> move_dirs;
    move_dirs['N'] = {1, 0};
    move_dirs['S'] = {-1, 0};
    move_dirs['W'] = {0, -1};
    move_dirs['E'] = {0, 1};

    long long x = 0, y = 0;
    long long times = 0;
    long long answer = 0;

    bool returned = false;
    for (int i = 0; i < N && !returned; i++) 
    {
        char dir;
        long long size;
        cin >> dir >> size;

        auto [dx, dy] = move_dirs[dir];

        for (long long step = 0; step < size; step++) 
        {
            x += dx;
            y += dy;
            times++;

            if (x == 0 && y == 0) 
            {
                answer = times;    
                returned = true;
                break;
            }
        }
    }

    if (!returned) answer = -1;

    cout << answer << "\n";
    return 0;
}