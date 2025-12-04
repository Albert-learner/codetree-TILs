#include <iostream>
#include <string>
using namespace std;

int main() 
{
    // Please write your code here.
    string input_str, find_chr;
    cin >> input_str >> find_chr;

    size_t pos = input_str.find(find_chr);

    if(pos == string::npos)
        cout << "No";
    else
        cout << pos;
        
    return 0;
}