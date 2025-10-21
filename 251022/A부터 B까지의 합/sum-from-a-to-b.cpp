#include <iostream>
using namespace std;

int main() 
{
    // Please write your code here.
    int a, b, sums = 0;
    cin >> a >> b;

    for(int i = a; i <= b; i++)
    {
        sums += i;
    }
    cout << sums;
    return 0;
}