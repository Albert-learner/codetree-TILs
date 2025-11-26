#include <iostream>
#include <string>
using namespace std;

int main() 
{
    // Please write your code here.
    string first, second;
    cin >> first >> second;

    if(first.length() > second.length())
        cout << first << ' ' << first.length();
    else if(first.length() < second.length())
        cout << second << ' ' << second.length();
    else    
        cout << "same";
    return 0;
} 