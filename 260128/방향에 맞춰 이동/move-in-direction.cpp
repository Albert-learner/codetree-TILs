#include <bits/stdc++.h>
using namespace std;

int main() 
{
    int n;
    cin >> n;

    long long mx = 0, my = 0;

    for (int i = 0; i < n; i++) 
    {
        char dir;
        long long dist;
        cin >> dir >> dist;

        if (dir == 'N') my += dist;
        else if (dir == 'S') my -= dist;
        else if (dir == 'E') mx += dist;
        else if (dir == 'W') mx -= dist;
    }

    cout << mx << " " << my << "\n";
    return 0;
}
