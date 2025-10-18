#include <iostream>
using namespace std;

int main() 
{
    // Please write your code here.
    int a, b;
    cin >> a >> b;

    while(a <= b)
    {
        if(a % 2 == 0)
            cout << a << ' ';
        a += 1;
    }
    
    return 0;
}