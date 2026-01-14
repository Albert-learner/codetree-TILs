#include <bits/stdc++.h>
using namespace std;

int main() 
{
    string bin_number;
    cin >> bin_number;

    // Please write your code here.
    long long num = 0;
    for(char c : bin_number)
    {
        int bit = c - '0';
        num = num * 2 + bit;
    }

    cout << num;
    return 0;
}