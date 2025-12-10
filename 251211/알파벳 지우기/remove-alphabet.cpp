#include <iostream>
#include <string>
#include <cctype>
using namespace std;

int main() 
{
    // Please write your code here.
    string first, second, n_first = "", n_second = "";
    int s_first = 0, s_second = 0;
    cin >> first >> second;

    for(char c: first)
    {
        if(isdigit(c))
            n_first += c;
    }
    for(char c: second)
    {
        if(isdigit(c))
            n_second += c;
    }

    s_first = stoi(n_first);
    s_second = stoi(n_second);

    cout << s_first + s_second;
    return 0;
}