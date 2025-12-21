#include <iostream>
#include <algorithm>
using namespace std;

int a, b;

int main() 
{
    cin >> a >> b;
    // Please write your code here.
    if(a > b)
    {
        a += 25;
        b *= 2;
    }
    else
    {
        b += 25;
        a *= 2;
    }
    cout << a << ' ' << b;

    return 0;
}