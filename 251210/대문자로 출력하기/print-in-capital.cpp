#include <iostream>
#include <string>
using namespace std;

int main() 
{
    // Please write your code here.
    string inp_str, result = "";
    cin >> inp_str;

    for(int i = 0; i < inp_str.size(); i++)
    {
        if(isalpha(inp_str[i]))
            result += inp_str[i];
    }

    for(int i = 0; i < result.size(); i++)
    {
        result[i] = toupper(result[i]);
    }
    cout << result;
    return 0;
}