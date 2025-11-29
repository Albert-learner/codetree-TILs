#include <bits/stdc++.h>
using namespace std;

int main() 
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N;
    cin >> N;
    cin.ignore();   

    vector<string> input_strs(N);
    for (int i = 0; i < N; i++) 
    {
        getline(cin, input_strs[i]);
    }

    int total_lengths = 0;
    int a_cnts = 0;

    for (const string &s : input_strs) 
    {
        total_lengths += s.length();
        if (!s.empty() && s[0] == 'a') 
        {
            a_cnts++;
        }
    }

    cout << total_lengths << " " << a_cnts;
    return 0;
}
