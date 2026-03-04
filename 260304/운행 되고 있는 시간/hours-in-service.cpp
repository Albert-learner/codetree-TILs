#include <bits/stdc++.h>
using namespace std;

int main() 
{
    int N;
    cin >> N;

    vector<pair<int,int>> developers(N);
    for (int i = 0; i < N; i++) 
    {
        int s, e;
        cin >> s >> e;
        developers[i] = {s, e};
    }

    // Please write your code here.
    int max_run_time = 0;

    for (int i = 0; i < N; i++) 
    {
        unordered_set<int> times;
        times.reserve(1024);

        for (int j = 0; j < N; j++) 
        {
            if (j == i) continue; 
            int start = developers[j].first;
            int end   = developers[j].second;

            for (int t = start; t < end; t++) 
            {
                times.insert(t);
            }
        }

        int sz = (int)times.size();
        if (sz > max_run_time) max_run_time = sz;
    }

    cout << max_run_time << "\n";
    return 0;
}