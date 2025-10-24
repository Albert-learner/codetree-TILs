#include <iostream>
using namespace std;

int main() 
{
    // Please write your code here.
    int a, b, n_mul = 1;
    cin >> a >> b;

    for(int i = a; i <= b; i++)
    {
        n_mul *= i;
    }
    cout << n_mul;
    return 0;
}