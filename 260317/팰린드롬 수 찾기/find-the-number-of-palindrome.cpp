#include <bits/stdc++.h>
using namespace std;

bool is_palindrome(const vector<int>& num) 
{
    return num == vector<int>(num.rbegin(), num.rend());
}

int main() 
{
    int X, Y;
    cin >> X >> Y;

    // Please write your code here.
    int cnts = 0;
    for (int num = X; num <= Y; num++) 
    {
        string s = to_string(num);
        vector<int> num_lst;
        for (char c : s) 
        {
            num_lst.push_back(c - '0');
        }

        if (is_palindrome(num_lst)) 
        {
            cnts += 1;
        }
    }
    cout << cnts;
    return 0;
}
