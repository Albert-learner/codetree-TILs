#include <iostream>
#include <algorithm>
using namespace std;

int main() 
{
    // Please write your code here.
    int a, b, c, min_cst;
    cin >> a >> b >> c;

    min_cst = min({a, b, c});
    cout << min_cst;
    
    return 0;
}