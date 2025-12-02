#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

int main() 
{
    // Please write your code here.
    string input_str;
    getline(cin, input_str);

    vector<char> eval_strs;

    for(int i = 0; i < input_str.length(); i++)
    {
        if((i + 1) % 2 == 0)
            eval_strs.push_back(input_str[i]);
    }

    reverse(eval_strs.begin(), eval_strs.end());

    for(char c: eval_strs)
        cout << c;
    return 0;
}