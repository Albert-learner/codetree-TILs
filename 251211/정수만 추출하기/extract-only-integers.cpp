#include <iostream>
#include <string>
#include <cctype>
using namespace std;

int main() 
{
    string first, second;
    cin >> first >> second;

    string first_str = "", second_str = "";

    for(char c : first) 
    {
        if(!isdigit(c)) break;
        first_str += c;
    }

    for(char c : second) 
    {
        if(!isdigit(c)) break;
        second_str += c;
    }

    int first_int = first_str.empty() ? 0 : stoi(first_str);
    int second_int = second_str.empty() ? 0 : stoi(second_str);

    cout << first_int + second_int;

    return 0;
}
