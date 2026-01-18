#include <bits/stdc++.h>
using namespace std;


int main() 
{
    int N;
    cin >> N;

    vector<pair<int,int>> lines_lst(N);
    for (int i = 0; i < N; i++) 
    {
        int start, end;
        cin >> start >> end;
        lines_lst[i] = {start, end};
    }

    unordered_map<int, int> inter_lines;
    inter_lines.reserve(200000); 

    for (auto &seg : lines_lst) 
    {
        int start = seg.first;
        int end = seg.second;
        for (int x = start; x < end; x++) 
        { 
            inter_lines[x] += 1;
        }
    }

    int ans = 0;
    for (auto &kv : inter_lines) 
    {
        ans = max(ans, kv.second);
    }

    cout << ans << "\n";
    return 0;
}