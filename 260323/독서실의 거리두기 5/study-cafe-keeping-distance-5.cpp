#include <bits/stdc++.h>
using namespace std;

int main() 
{
    // Please write your code here.
    int N;
    cin >> N;
    
    string s;
    cin >> s;
    vector<char>bin_str_lst(s.begin(), s.end());

    int answer = 0;
    for(int i = 0; i < N; i++)
    {
        if(bin_str_lst[i] == '1')
            continue;

        int tmp = INT_MAX;
        vector<int> fill_poses;

        for(int j = 0; j < N; j++)
        {
            if(bin_str_lst[j] == '1' || i == j)
                fill_poses.push_back(j);
        }

        for(int j = 0; j + 1 < (int)fill_poses.size(); j++)
            tmp = min(tmp, fill_poses[j + 1] - fill_poses[j]);

        answer = max(answer, tmp);
    }
    cout << answer;
    return 0;
}