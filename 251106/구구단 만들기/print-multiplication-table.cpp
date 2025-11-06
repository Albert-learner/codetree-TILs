#include <iostream>
using namespace std;

int main() 
{
    // Please write your code here.
    int a, b;
    cin >> a >> b;

    for(int i = 1; i < 10; i++)
    {
        if(a != b)
        {
            for(int n = b; n > a - 1; n -= 2)
            {
                if(n == a)
                    cout << n << " * " << i << " = " << n * i << endl;
                else
                    cout << n << " * " << i << " = " << n * i << " / ";
            }
        }
        else
        {
            cout << a << " * " << i << " = " << a * i << endl;
        }
    }
    return 0;
}