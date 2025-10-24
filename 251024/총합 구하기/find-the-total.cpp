#include <iostream>
using namespace std;

int main() 
{
    // Please write your code here.
    int a, b, c_sum = 0;
    cin >> a >> b;

    for(int i = a; i <= b; i++)
    {
        if(i % 6 == 0 && i % 8 != 0)
            c_sum += i;
    }
    cout << c_sum;
    return 0;
}