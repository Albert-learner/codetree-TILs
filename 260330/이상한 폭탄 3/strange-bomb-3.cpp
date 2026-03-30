#include <bits/stdc++.h>
using namespace std;


int main()
{
    int N, K;
    cin >> N >> K;

    vector<int> bombs(N);
    for (int i = 0; i < N; i++) 
    {
        cin >> bombs[i];
    }

    unordered_map<int, int> last_idx;
    unordered_map<int, int> explosions;

    for (int i = 0; i < N; i++) 
    {
        if (last_idx.find(bombs[i]) != last_idx.end()) 
        {
            if (i - last_idx[bombs[i]] <= K) 
            {
                explosions[bombs[i]]++;
            }
        }
        last_idx[bombs[i]] = i;
    }

    int answer = 0;
    int best_count = -1;

    for (const auto& kv : explosions) 
    {
        int bomb_num = kv.first;
        int cnt = kv.second;

        if (cnt > best_count)
        {
            best_count = cnt;
            answer = bomb_num;
        } 
        else if (cnt == best_count && bomb_num > answer) 
        {
            answer = bomb_num;
        }
    }

    cout << answer << '\n';
    return 0;
}