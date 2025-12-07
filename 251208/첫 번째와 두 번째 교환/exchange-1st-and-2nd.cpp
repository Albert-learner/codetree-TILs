#include <iostream>
#include <string>
using namespace std;

int main() 
{
    string input_str;
    cin >> input_str;

    if(input_str.length() >= 2)
    {
        char temp = input_str[0];
        input_str[0] = input_str[1];
        input_str[1] = temp;
    }

    for(int idx = 2; idx < input_str.length(); idx++)
    {
        if(input_str[idx] == input_str[0]) 
        {
            input_str[idx] = input_str[1];
        }
        else if(input_str[idx] == input_str[1]) 
        {
            input_str[idx] = input_str[0];
        }
    }

    cout << input_str;
    return 0;
}

