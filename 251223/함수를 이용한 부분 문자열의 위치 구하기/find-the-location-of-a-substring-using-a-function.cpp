#include <iostream>
#include <string>

using namespace std;

string text;
string pattern;

int main() 
{
    cin >> text;
    cin >> pattern;

    // Please write your code here.
    size_t pos = text.find(pattern);
    if(pos != string::npos)
        cout << pos;
    else
        cout << -1;
    
    return 0;
}