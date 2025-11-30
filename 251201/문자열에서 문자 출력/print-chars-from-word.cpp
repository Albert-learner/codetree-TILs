#include <iostream>
#include <string>
using namespace std;

int main() 
{
    // Please write your code here.
    string input_str;
    cin >> input_str;

    for(int i = 0; i < input_str.length(); i++)
    {
        cout << input_str[i] << endl;
    }
    return 0;
}