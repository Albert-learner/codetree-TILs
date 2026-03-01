#include <bits/stdc++.h>
using namespace std;

bool is_interest_num(long long num) 
{
    string s = to_string(num);
    int freq[10] = {0};

    for (char ch : s) freq[ch - '0']++;

    vector<int> cnts;
    for (int d = 0; d < 10; d++) 
    {
        if (freq[d] > 0) cnts.push_back(freq[d]);
    }

    if ((int)cnts.size() != 2) return false;

    int total = (int)s.size();
    return ( (cnts[0] == total - 1 && cnts[1] == 1) ||
             (cnts[0] == 1 && cnts[1] == total - 1) );
}

int main() 
{
    long long X, Y;
    cin >> X >> Y;

    long long ans = 0;
    for (long long num = X; num <= Y; num++) 
    {
        if (is_interest_num(num)) ans++;
    }

    cout << ans << "\n";
    return 0;
}