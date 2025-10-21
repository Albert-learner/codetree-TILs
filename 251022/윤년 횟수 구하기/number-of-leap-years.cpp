#include <iostream>
using namespace std;

int main() 
{
    // Please write your code here.
    int n, cnts = 0;
    cin >> n;

    for(int i = 1; i <= n; i++)
    {
        if(i % 4 == 0)
        {
            if(i % 100 == 0 && i % 400 != 0)
                continue;
            else
                cnts += 1;
        }
    }
    cout << cnts;
    return 0;
}