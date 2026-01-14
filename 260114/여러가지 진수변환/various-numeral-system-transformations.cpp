#include <bits/stdc++.h>
using namespace std;

int main() 
{
    long long N;
    int base;
    cin >> N >> base;

    // Please write your code here.
    vector<long long> digits;
    while (true) 
    {
        if (N < base) 
        {
            digits.push_back(N);
            break;
        }
        digits.push_back(N % base);
        N /= base;
    }

    for (int i = (int)digits.size() - 1; i >= 0; --i) 
    {
        cout << digits[i];
    }
    return 0;
}