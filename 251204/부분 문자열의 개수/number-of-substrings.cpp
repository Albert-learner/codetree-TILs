#include <iostream>
#include <string>
using namespace std;

int main() 
{
    // Please write your code here.
    string a_str, b_str;
    int answer = 0, a_len, b_len;

    getline(cin, a_str);
    getline(cin, b_str);

    a_len = a_str.length();
    b_len = b_str.length();

    for(int i = 0; i < a_len - b_len + 1; i++)
    {
        if(a_str.substr(i, b_len) == b_str)
            answer += 1;
    }

    cout << answer;
    return 0;
}