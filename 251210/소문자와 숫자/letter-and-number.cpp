#include <iostream>
#include <string>
#include <cctype>
using namespace std;

int main() 
{
    string input_str;
    getline(cin, input_str);

    for(char c : input_str) 
    {
        if(isalpha(c) || isdigit(c)) 
        {
            cout << (char)tolower(c);
        }
    }
    return 0;
}
