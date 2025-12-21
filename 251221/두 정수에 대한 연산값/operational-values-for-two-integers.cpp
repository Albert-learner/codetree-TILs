#include <iostream>
#include <algorithm>
using namespace std;

int a, b;

int main() 
{
    cin >> a >> b;
    int max_n, min_n;
    // Please write your code here.
    max_n = max(a, b) + 25;
    min_n = min(a, b) * 2;

    cout << min_n << ' ' << max_n;
    return 0;
}