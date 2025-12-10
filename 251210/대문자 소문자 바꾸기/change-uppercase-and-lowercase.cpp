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
        if(islower(c)) 
        {
            cout << (char)toupper(c);
        }
        else if(isupper(c)) 
        {
            cout << (char)tolower(c);
        }
    }

    return 0;
}
