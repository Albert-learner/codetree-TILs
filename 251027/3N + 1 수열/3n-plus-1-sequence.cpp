#include <iostream>
using namespace std;

int main() 
{
    // Please write your code here.
    int n, cnts = 0;
    cin >> n;

    while(n != 1)
    {
        if(n % 2 == 0)
            n /= 2;
        else
        {
            n *= 3;
            n += 1;
        }
        cnts += 1;
    }
    cout << cnts;
    return 0;
}