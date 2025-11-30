#include <iostream>
#include <string>
#include <algorithm>
using namespace std;

int main() 
{
    // Please write your code here.
    int idx;
    string input_str;
    cin >> input_str;
    cin >> idx;

    reverse(input_str.begin(), input_str.end());
    for(int i = 0; i < idx; i++)
    {
        cout << input_str[i];
    }
    return 0;
}