#include <bits/stdc++.h>
using namespace std;


int main() 
{
    long long N, T;
    cin >> N >> T;

    long long x, y;
    char dir;
    cin >> x >> y >> dir;

    x--; y--;

    auto dx = [&](char d) -> long long 
    {
        if (d == 'U') return -1;
        if (d == 'D') return 1;
        return 0;
    };
    auto dy = [&](char d) -> long long 
    {
        if (d == 'L') return -1;
        if (d == 'R') return 1;
        return 0;
    };

    auto reverse_dir = [&](char d) -> char 
    {
        if (d == 'L') return 'R';
        if (d == 'R') return 'L';
        if (d == 'U') return 'D';
        return 'U'; // 'D'
    };

    while (T-- > 0) 
    {
        if (0 <= x && x < N && 0 <= y && y < N) 
        {
            long long nx = x + dx(dir);
            long long ny = y + dy(dir);

            if (0 <= nx && nx < N && 0 <= ny && ny < N) 
            {
                x = nx;
                y = ny;
            } 
            else 
            {
                dir = reverse_dir(dir);
            }
        }
    }

    cout << (x + 1) << " " << (y + 1) << "\n";
    return 0;
}
