#include <iostream>
using namespace std;

int main() 
{
    // Please write your code here.
    int a, b;
    cin >> a >> b;

    if(a > 0)
    {
        for(int i = 0; i < b; i++)
        {
            cout << a;
        }
    }
    else
        cout << 0;
    return 0;
}