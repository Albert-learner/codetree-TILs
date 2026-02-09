#include <bits/stdc++.h>
using namespace std;

int main() 
{
    string a;
    cin >> a;

    // Please write your code here.
    vector<int> a_bin;
    a_bin.reserve(a.size());
    for(char ch: a) a_bin.push_back(ch - '0');

    bool indicator = true;
    for (size_t i = 0; i < a_bin.size(); i++) 
    {
        if (a_bin[i] == 0) 
        {
            a_bin[i] = 1;
            indicator = false;
            break;
        }
    }

    long long num = 0;
    for (size_t i = 0; i < a_bin.size(); i++) 
    {
        num = num * 2 + a_bin[i];
    }

    if (indicator) cout << num - 1 << "\n";
    else cout << num << "\n";
    return 0;
}