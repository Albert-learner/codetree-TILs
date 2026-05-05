#include <bits/stdc++.h>
using namespace std;

int main() 
{
    // Please write your code here.
    int x1, y1, x2, y2, a1, b1, a2, b2;
    cin >> x1 >> y1 >> x2 >> y2;
    cin >> a1 >> b1 >> a2 >> b2;

    int min_x = min({x1, x2, a1, a2}), min_y = min({y1, y2, b1, b2});
    int max_x = max({x1, x2, a1, a2}), max_y = max({y1, y2, b1, b2});

    cout << int(abs(max_x - min_x)) * int(abs(max_y - min_y));
    return 0;
}