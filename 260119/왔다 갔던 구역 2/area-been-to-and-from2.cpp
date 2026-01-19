#include <bits/stdc++.h>
using namespace std;

int main() 
{
    int N;
    cin >> N;

    long long cur_pos = 0;
    unordered_map<long long, int> visited;
    visited.reserve(200000);

    for (int _ = 0; _ < N; _++) 
    {
        long long size;
        char mv_dir;
        cin >> size >> mv_dir;

        if (mv_dir == 'R') 
        {
            for (long long i = 0; i < size; i++) 
            {
                visited[cur_pos + i]++;  
            }
            cur_pos += size;
        } 
        else if (mv_dir == 'L') 
        {
            for (long long i = 1; i <= size; i++) 
            {
                visited[cur_pos - i]++;
            }
            cur_pos -= size;
        }
    }

    long long cnts = 0;
    for (auto &kv : visited) {
        if (kv.second >= 2) cnts++;
    }

    cout << cnts << "\n";
    return 0;
}