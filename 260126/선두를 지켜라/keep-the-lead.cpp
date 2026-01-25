#include <bits/stdc++.h>
using namespace std;

int main() 
{
    int N, M;
    cin >> N >> M;

    vector<long long> a_dist(1, 0), b_dist(1, 0);

    auto make_dist = [&](int p_num, vector<long long>& which_dist)
    {
        for(int i = 0; i < p_num; i++)
        {
            long long velocity;
            int times;
            cin >> velocity >> times;
            for(int j = 0; j < times; j++)
                which_dist.push_back(which_dist.back() + velocity);
        }
    };

    // Please write your code here.
    make_dist(N, a_dist);
    make_dist(N, b_dist);

    vector<long long> compare;
    compare.reserve(min(a_dist.size(), b_dist.size()));
    size_t L = min(a_dist.size(), b_dist.size());
    for (size_t i = 0; i < L; i++) 
    {
        if (a_dist[i] != b_dist[i]) 
        {
            compare.push_back(a_dist[i] - b_dist[i]);
        }
    }

    long long answer = 0;
    for (size_t i = 1; i < compare.size(); i++) 
    {
        if (compare[i] * compare[i - 1] < 0) 
        {
            answer++;
        }
    }

    cout << answer << "\n";

    return 0;
}