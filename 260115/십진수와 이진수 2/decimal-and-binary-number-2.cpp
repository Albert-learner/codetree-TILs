#include <bits/stdc++.h>
using namespace std;

int main() 
{
    string bin_number;
    cin >> bin_number;

    // Please write your code here.
    long long num = 0;
    for(char ch: bin_number)
    {
        num = num * 2 + (ch - '0');
    }
    num *= 17;

    if (num == 0) 
    {
        cout << 0;
        return 0;
    }

    string digits;
    while (num > 0) 
    {
        digits.push_back(char('0' + (num % 2)));
        num /= 2;
    }
    reverse(digits.begin(), digits.end());

    cout << digits;
    return 0;
}