#include <bits/stdc++.h>
using namespace std;

int main() 
{
    // Please write your code here.
    int N;
    cin >> N;
    vector<long long> blocks(N);
    for (int i = 0; i < N; i++) 
    {
        cin >> blocks[i];
    }

    long long sum_blocks = 0;
    for (auto b : blocks) sum_blocks += b;

    long long average = sum_blocks / N;

    long long cnts = 0;

    while (true) 
    {
        bool done = true;
        for (int i = 0; i < N; i++) 
        {
            if (blocks[i] != average) 
            {
                done = false;
                break;
            }
        }
        if (done) break;

        sort(blocks.begin(), blocks.end());

        long long diff = average - blocks[0];
        long long diff_max = llabs(average - blocks[N - 1]);

        blocks[0] += diff;
        blocks[N - 1] -= diff_max;

        cnts += diff;
    }

    cout << cnts << '\n';
    return 0;
}