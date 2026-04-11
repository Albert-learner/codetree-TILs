#include <bits/stdc++.h>
using namespace std;

struct EatCheezes 
{
    int p, m, t;
};

struct AcheTimes 
{
    int p, t;
};

int main() 
{
    int N, M, D, S;
    cin >> N >> M >> D >> S;

    vector<EatCheezes> eat_cheezes(D);
    for (int i = 0; i < D; i++) 
    {
        cin >> eat_cheezes[i].p >> eat_cheezes[i].m >> eat_cheezes[i].t;
    }

    vector<AcheTimes> ache_times(S);
    for (int i = 0; i < S; i++) 
    {
        cin >> ache_times[i].p >> ache_times[i].t;
    }

    // Please write your code here.
    int max_medicines = 0;

    for (int i = 1; i <= M; i++) 
    {
        vector<int> time(N + 1, 0);
        for (const auto& e : eat_cheezes) 
        {
            if (e.m != i) continue;
            int person = e.p;
            if (time[person] == 0 || time[person] > e.t) 
            {
                time[person] = e.t;
            }
        }

        bool possible = true;
        for (const auto& a : ache_times) 
        {
            int person = a.p;
            if (time[person] == 0 || time[person] >= a.t) 
            {
                possible = false;
                break;
            }
        }

        if (possible) 
        {
            int medicines = 0;
            for (int j = 1; j <= N; j++) 
            {
                if (time[j] != 0) medicines++;
            }
            max_medicines = max(max_medicines, medicines);
        }
    }

    cout << max_medicines << "\n";
    return 0;
}