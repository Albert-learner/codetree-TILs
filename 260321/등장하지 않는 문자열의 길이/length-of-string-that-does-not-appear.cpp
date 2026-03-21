#include <bits/stdc++.h>
using namespace std;

int main() 
{
    int N;
    cin >> N;

    string n_str;
    cin >> n_str;

    map<string, int> pattern_cnts;

    for (int s_len = 1; s_len < N; s_len++) 
    {
        for (int chr_idx = 0; chr_idx <= N - s_len; chr_idx++) 
        {
            string sub = n_str.substr(chr_idx, s_len);
            pattern_cnts[sub]++;
        }
    }
    // Please write your code here.
    vector<vector<pair<string, int>>> patterns;
    int max_length = 0;
    for (const auto& p : pattern_cnts) 
    {
        max_length = max(max_length, (int)p.first.size());
    }

    for (int length = 1; length <= max_length; length++) 
    {
        vector<pair<string, int>> tmp;
        for (const auto& p : pattern_cnts) 
        {
            if ((int)p.first.size() == length) 
            {
                tmp.push_back({p.first, p.second});
            }
        }
        if (!tmp.empty()) 
        {
            patterns.push_back(tmp);
        }
    }

    sort(patterns.begin(), patterns.end(),
         [](const vector<pair<string, int>>& a, const vector<pair<string, int>>& b) 
         {
             return a[0].second > b[0].second;
         });

    int min_length = 0;

    for (const auto& pattern_lst : patterns) 
    {
        bool all_less_than_2 = true;
        for (const auto& p : pattern_lst) 
        {
            if (p.second >= 2) 
            {
                all_less_than_2 = false;
                break;
            }
        }

        if (all_less_than_2) 
        {
            min_length = (int)pattern_lst[0].first.size();
            break;
        }
    }

    cout << min_length << '\n';
    return 0;
}