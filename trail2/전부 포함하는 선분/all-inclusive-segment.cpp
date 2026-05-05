#include <iostream>
#include <vector>
#include <algorithm>
#include <climits>
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

    int min_line = INT_MAX;

    for (int i = 0; i < N; i++) 
    {
        vector<pair<int, int>> excludeds;

        for (int j = 0; j < N; j++) 
        {
            if (i != j) 
            {
                excludeds.push_back(lines[j]);
            }
        }

        sort(excludeds.begin(), excludeds.end());

        int start = INT_MAX;
        int end = INT_MIN;

        for (auto &p : excludeds) 
        {
            start = min(start, p.first);
            end = max(end, p.second);
        }

        min_line = min(min_line, end - start);
    }

    cout << min_line << '\n';

    return 0;
}