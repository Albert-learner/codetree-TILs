#include <iostream>
using namespace std;

int main() 
{
    // Please write your code here.
    int n, cls = 0, flr = 0, rst = 0;
    cin >> n;

    for(int i = 1; i <= n; i++)
    {
        if(i % 12 == 0)
            rst += 1;
        else if(i % 3 == 0)
            flr += 1;
        else if(i % 2 == 0)
            cls += 1;
    }

    cout << cls << ' ' << flr << ' ' << rst;
    return 0;
}