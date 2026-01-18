#include <bits/stdc++.h>
using namespace std;

int main() 
{
    int N, K;
    cin >> N >> K;

    vector<pair<int,int>> blocks(K);
    for (int i = 0; i < K; i++) 
    {
        int first, second;
        cin >> first >> second;
        blocks[i] = {first, second};
    }

    // Please write your code here.
    vector<int> checked(N + 1, 0);
    for (auto [start, end] : blocks) 
    {
        for (int i = start; i <= end; i++) 
        {
            checked[i] += 1;
        }
    }

    cout << *max_element(checked.begin(), checked.end()) << "\n";
    return 0;
}