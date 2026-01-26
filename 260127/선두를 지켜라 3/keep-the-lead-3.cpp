#include <bits/stdc++.h>
using namespace std;

static void make_dist(int player, vector<long long>& dist) 
{
    for (int i = 0; i < player; i++) 
    {
        long long velocity;
        int times;
        cin >> velocity >> times;
        for (int t = 0; t < times; t++) 
        {
            dist.push_back(dist.back() + velocity);
        }
    }
}

int main() 
{
    int N, M;
    cin >> N >> M;

    vector<long long> a_dist(1, 0), b_dist(1, 0);

    make_dist(N, a_dist);
    make_dist(M, b_dist);

    // Please write your code here.
    long long cnts = 0;
    int key = 0;
    int prev_key = -100;

    for (size_t i = 1; i < a_dist.size(); i++) 
    {
        if (a_dist[i] > b_dist[i]) key = -1;
        else if (a_dist[i] == b_dist[i]) key = 0;
        else key = 1;

        if (key != prev_key) cnts++;
        prev_key = key;
    }

    cout << cnts << "\n";
    return 0;
}