#include <iostream>
#include <string>
using namespace std;

int main() 
{
    string input_str;
    getline(cin, input_str);

    char from = input_str[1];
    char to = input_str[0];

    for(char &c : input_str) 
    {
        if(c == from) c = to;
    }

    cout << input_str;
    return 0;
}
