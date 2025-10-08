#include <iostream>
using namespace std;

int main() 
{
    // Please write your code here.
    int n;
    cin >> n;

    if(n >= 100)
        cout << "vapor";
    else if(0 <= n and n < 100)
        cout << "water";
    else    
        cout << "ice";
    return 0;
}