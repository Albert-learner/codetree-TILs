#include <iostream>
using namespace std;

int main() 
{
    // Please write your code here.
    int a, b, a_muls = 1;
    cin >> a >> b;

    for(int i = 1; i <= b; i++)
    {
        if(i % a == 0)
            a_muls *= i;
    }
    cout << a_muls;
    return 0;
}