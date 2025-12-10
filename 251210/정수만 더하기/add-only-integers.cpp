#include <iostream>
#include <string>
#include <cctype>
using namespace std;

int main() 
{
    string a_str;
    cin >> a_str;

    int total = 0;
    for(char c : a_str) 
    {
        if(isdigit(c)) 
        {
            total += c - '0';
        }
    }

    cout << total;
    return 0;
}
