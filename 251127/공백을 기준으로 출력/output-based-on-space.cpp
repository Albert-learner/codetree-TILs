#include <iostream>
#include <vector>
#include <string>
using namespace std;

int main() 
{
    vector<string> first, second;
    string word;

    while (cin >> word) 
    {
        first.push_back(word);
        if (cin.peek() == '\n') break;
    }

    while (cin >> word) 
    {
        second.push_back(word);
        if (cin.peek() == '\n') break;
    }

    for (const string &s : first) 
    {
        cout << s;
    }
    for (const string &s : second) 
    {
        cout << s;
    }

    return 0;
}
