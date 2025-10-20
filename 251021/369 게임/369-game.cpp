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
        string s = to_string(i);
        if(i % 3 == 0 || s.find('3') != string::npos || s.find('6') != string::npos || s.find('9') != string::npos)
            cout << 0 << ' ';
        else
            cout << i << ' ';
    }

    return 0;
}