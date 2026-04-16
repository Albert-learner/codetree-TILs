#include <bits/stdc++.h>
using namespace std;

int get_min_diff(const vector<int>& lst)
{
    int cnts = 0;
    vector<int> diffs;

    for(int j = 0; j < (int)lst.size(); j++)
    {
        if(lst[j] == 1)
        {
            diffs.push_back(cnts);
            cnts = 0;
        }
        cnts += 1;
    }

    int mn = 1e9;
    for(int i = 1; i < (int)diffs.size(); i++)
        mn = min(mn, diffs[i]);

    return mn;
}

int main() 
{
    // Please write your code here.
    int N;
    cin >> N;

    string s;
    cin >> s;

    vector<int>seats;
    for(char c : s)
        seats.push_back(c - '0');

    int max_dst = -1;
    for(int i = 0; i < N; i++)
    {
        if(seats[i] == 0)
        {
            seats[i] = 1;
            max_dst = max(max_dst, get_min_diff(seats));
            seats[i] = 0;
        }
    }

    cout << max_dst << endl;
    return 0;
}
