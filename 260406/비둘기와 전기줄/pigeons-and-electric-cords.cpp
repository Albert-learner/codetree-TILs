#include <bits/stdc++.h>
using namespace std;

int main() 
{
    // Please write your code here.
    int N;
    cin >> N;
    vector<pair<int, int>> birds(N);
    for(int i = 0; i < N; i++)
        cin >> birds[i].first >> birds[i].second;

    sort(birds.begin(), birds.end(), [](const pair<int,int>& a, const pair<int,int>& b) {
        return a.first < b.first;
        });

    int cnts = 0;
    pair<int, int> cur_bird = birds[0];

    for(int i = 1; i < N; i++)
    {
        if(birds[i].first != cur_bird.first)
            cur_bird = birds[i];
        else
        {
            if(birds[i].second != cur_bird.second)
            {
                cur_bird = birds[i];
                cnts++;
            }
        }
    }

    cout << cnts << '\n';
    return 0;
}