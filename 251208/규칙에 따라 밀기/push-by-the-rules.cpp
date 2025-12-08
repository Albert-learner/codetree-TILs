#include <iostream>
#include <string>
using namespace std;

int main() 
{
    // Please write your code here.
    string a_str, cmds;
    getline(cin, a_str);
    getline(cin, cmds);

    for(int i = 0; i < cmds.length(); i++)
    {
        if(cmds[i] == 'L')
        {
            a_str = a_str.substr(1) + a_str[0];
        }
        else if(cmds[i] == 'R')
        {
            a_str = a_str.back() + a_str.substr(0, a_str.size() - 1);
        }
    }
    cout << a_str;
    return 0;
}