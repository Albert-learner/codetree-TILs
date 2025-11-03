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
        for(int j = 0; j < n; j++)
        {
            cout << to_string(i);
        }
        cout << endl;
    }
    return 0;
}