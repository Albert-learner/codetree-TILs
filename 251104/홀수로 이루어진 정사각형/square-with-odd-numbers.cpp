#include <iostream>
#include <string>
using namespace std;

int main() 
{
    // Please write your code here.
    int n;
    cin >> n;

    for(int i = 0; i < 2 * n; i += 2)
    {
        for(int j = 11; j < 2 * n - 1 + 11; j += 2)
        {
            cout << i + j << ' ';
        }
        cout << endl;
    }
    return 0;
}