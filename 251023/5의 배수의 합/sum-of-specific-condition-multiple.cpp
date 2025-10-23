#include <iostream>
using namespace std;

int main() 
{
    // Please write your code here.
    int a, b, five_sum = 0;
    cin >> a >> b;

    if(a >= b)
    {
        for(int i = b; i <= a; i++)
        {
            if(i % 5 == 0)
                five_sum += i;
        }
    }
    else
    {
        for(int i = a; i <= b; i++)
        {
            if(i % 5 == 0)
                five_sum += i;
        }
    }

    cout << five_sum;
    return 0;
}