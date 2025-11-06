#include <iostream>
using namespace std;

int main() 
{
    // Please write your code here.
    int a, b;
    cin >> a >> b;

    for(int j = 2; j < 9; j += 2)
    {
        for(int i = b; i > a - 1; i--)
        {
            if(i == a)
                cout << i << " * " << j << " = " << i * j << endl;
            else
                cout << i << " * " << j << " = " << i * j << " / ";
        }
    }
    return 0;
}