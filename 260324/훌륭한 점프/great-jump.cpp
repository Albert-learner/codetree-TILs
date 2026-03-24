#include <bits/stdc++.h>
using namespace std;

int N, K;
vector<int> stones;

bool jump_possible(int min_val) 
{
    int cnts = 0;
    vector<int> available_stones(100, 0);

    for (int i = 0; i < N; i++) 
    {
        if (stones[i] <= min_val) 
        {
            available_stones[cnts] = i;
            cnts += 1;
        }
    }

    for (int i = 1; i < cnts; i++) 
    {
        if (available_stones[i] - available_stones[i - 1] > K) {
            return false;
        }
    }

    return true;
}

int main() {
    cin >> N >> K;
    stones.resize(N);
    for (int i = 0; i < N; i++) 
    {
        cin >> stones[i];
    }

    int maxmin_cst = INT_MAX;

    for (int stone = 100; stone >= max(stones[0], stones[N - 1]); stone--) 
    {
        if (jump_possible(stone)) 
        {
            maxmin_cst = min(maxmin_cst, stone);
        }
    }

    cout << maxmin_cst << '\n';
    return 0;
}