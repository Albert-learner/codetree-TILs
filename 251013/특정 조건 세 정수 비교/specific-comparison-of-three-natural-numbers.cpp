#include <iostream>
#include <algorithm>
using namespace std;

int main() 
{
    // Please write your code here.
    int a, b, c, min_cst;
    cin >> a >> b >> c;

    min_cst = min({a, b, c});
    if(a == min_cst)
        cout << 1 << ' ';
    else
        cout << 0 << ' ';

    if(a == b && b == c)
        cout << 1;
    else
        cout << 0;
        
    return 0;
}