#include <iostream>
using namespace std;

int main() 
{
    // Please write your code here.
    int n;
    cin >> n;

    for(int i = 0; i < n; i++)
    {
        for(int j = n - i; j < n + 1; j++)
            cout << j << ' ';
        cout << endl;
    }
    return 0;
}