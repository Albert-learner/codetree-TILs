#include <bits/stdc++.h>
using namespace std;

int main() 
{
    int N;
    cin >> N;
    vector<pair<int, int>> lines(N);
    for (int i = 0; i < N; i++) 
    {
        cin >> lines[i].first >> lines[i].second;
    }

    vector<int> total_line(101, 0);

    for (auto &line : lines) 
    {
        int x = line.first;
        int y = line.second;
        for (int i = x; i <= y; i++) 
        {
            total_line[i] += 1;
        }
    }

    bool found = false;
    for (int i = 0; i < 101; i++) 
    {
        if (total_line[i] == N) 
        {
            found = true;
            break;
        }
    }

    if (found) 
    {
        cout << "Yes\n";
    } else {
        cout << "No\n";
    }
    return 0;
}