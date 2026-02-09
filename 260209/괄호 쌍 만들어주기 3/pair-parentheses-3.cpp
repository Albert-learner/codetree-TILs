#include <bits/stdc++.h>
#include <string>
using namespace std;

int main() 
{
    string a_str;
    cin >> a_str;

    // Please write your code here.
    int answer = 0;
    for(int i = 0; i < a_str.length(); i++)
    {
        for(int j = i + 1; j < a_str.length(); j++)
        {
            if(a_str[i] == '(' && a_str[j] == ')')
                answer += 1;
        }
    }
    cout << answer;
    return 0;
}