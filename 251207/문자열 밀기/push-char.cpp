#include <iostream>
#include <string>
using namespace std;

int main() 
{
    string input_str;
    cin >> input_str;

    if (input_str.length() > 1) 
    {
        cout << input_str.substr(1) + input_str[0];
    } 
    else 
    {
        cout << input_str;  
    }

    return 0;
}
