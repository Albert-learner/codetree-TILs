#include <iostream>
#include <string>
using namespace std;

int main() 
{
    string input_str, find_str;
    getline(cin, input_str);  
    getline(cin, find_str); 

    size_t pos = input_str.find(find_str);

    if (pos == string::npos) 
    {
        cout << -1;
    } 
    else 
    {
        cout << pos;
    }

    return 0;
}
