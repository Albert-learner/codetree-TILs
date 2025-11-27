#include <iostream>
#include <string>
using namespace std;

int main() 
{
    // Please write your code here.
    string input_str;
    getline(cin, input_str);

    for(int i = 2; i < 10 && i < input_str.length(); i++)
    {
        cout << input_str[i];
    }
    return 0;
}