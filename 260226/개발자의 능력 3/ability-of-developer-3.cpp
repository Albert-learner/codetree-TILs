#include <bits/stdc++.h>
#include <numeric>
using namespace std;

int main() 
{
    vector<long long> abilities;
    long long x;

    while (cin >> x) abilities.push_back(x);

    // Please write your code here.
    int n = (int)abilities.size();
    long long total = 0;
    for (auto v : abilities) total += v;

    long long min_diff = 1000001; 
    for (int i = 0; i < n; i++) 
    {
        for (int j = i + 1; j < n; j++) 
        {
            for (int k = j + 1; k < n; k++) 
            {
                long long sum1 = abilities[i] + abilities[j] + abilities[k];
                long long sum2 = total - sum1;
                min_diff = min(min_diff, llabs(sum1 - sum2));
            }
        }
    }

    cout << min_diff << "\n";
    return 0;
}