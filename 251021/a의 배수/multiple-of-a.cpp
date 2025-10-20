#include <iostream>
using namespace std;

int main() 
{
    // Please write your code here.
    int n, a, i = 1;
    cin >> n >> a;

    while(i <= n)
    {
        if(i % a == 0)
            cout << 1 << endl;
        else
            cout << 0 << endl;

        i += 1;
    }

    return 0;
}