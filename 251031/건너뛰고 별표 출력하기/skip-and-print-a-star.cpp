#include <iostream>
#include <string>
using namespace std;

int main() 
{
    // Please write your code here.
    int n;
    cin >> n;

    for(int i = 1; i <= n; i++)
    {
        cout << string(i, '*') << endl << endl;
    }

    for(int i = n - 1; i > 0; i--)
    {
        cout << string(i, '*') << endl << endl;
    }
    return 0;
}