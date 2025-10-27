#include <iostream>
using namespace std;

int main() 
{
    // Please write your code here.
    int n, cnts = 0;
    cin >> n;
    
    while(n >= 2)
    {
        n /= 2;
        cnts += 1;
    }
    cout << cnts;
    return 0;
}