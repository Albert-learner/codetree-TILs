#include <iostream>
using namespace std;

int main() 
{
    // Please write your code here.
    int a, b;
    cin >> b >> a;

    while(b >= a)
    {
        if(b % 2 == 0)
        {
            cout << b << ' ';
            b -= 2;
        }
        else
            b -= 1;
            
    }
    return 0;
}