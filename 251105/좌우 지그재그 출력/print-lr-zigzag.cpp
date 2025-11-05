#include <iostream>
using namespace std;

int main() 
{
    // Please write your code here.
    int n;
    cin >> n;

    for(int i = 1; i <= n; i++)
    {
        if(i % 2 == 1)
        {
            for(int j = n * i - (n - 1); j < n * i + 1; j++)
            {
                cout << j << ' ';
            }
        }
        else
        {
            for(int j = n * i; j > n * i - n; j--)
            {
                cout << j << ' ';
            }
        }
        cout << endl;
    }
    return 0;
}