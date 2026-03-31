#include <bits/stdc++.h>
using namespace std;

int main() 
{
    // Please write your code here.
    int x1, x2, x3, x4;
    cin >> x1 >> x2 >> x3 >> x4;

    if (x2 > x4) 
    {
        swap(x1, x3);
        swap(x2, x4);
    }

    if (x2 >= x3) 
    {
        cout << "intersecting\n";
    } 
    else 
    {
        cout << "nonintersecting\n";
    }
    return 0;
}