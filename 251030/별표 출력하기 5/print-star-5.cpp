#include <iostream>
#include <string>
using namespace std;

int main() 
{
    // Please write your code here.
    int n;
    cin >> n;

    for(int i = n; i >= 1; i--)
    {
        string line;
        for(int j = 0; j < i; j++)
        {
            line += string(i, '*') + " ";
        }
        cout << line << endl;
    }
    return 0;
}