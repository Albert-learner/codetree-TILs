#include <bits/stdc++.h>
using namespace std;


int main() 
{
    long long A, B;
    cin >> A >> B;

    string N;
    cin >> N;

    // Please write your code here.
    long long num = 0;
    for (char c : N) 
    {
        int digit = c - '0';          
        num = num * A + digit;
    }

    if (num == 0) 
    {
        cout << 0;
        return 0;
    }

    vector<int> digits;
    while (num > 0) 
    {
        digits.push_back((int)(num % B));
        num /= B;
    }
    reverse(digits.begin(), digits.end());

    for (int d : digits) cout << d;
    
    return 0;
}
