#include <bits/stdc++.h>
using namespace std;

int main() 
{
    vector<long long> developers;
    long long x;

    while (cin >> x) 
    {
        developers.push_back(x);
    }

    sort(developers.begin(), developers.end());

    int n = (int)developers.size();
    vector<long long> result;
    result.reserve(n / 2);

    for (int i = 0; i < n / 2; i++) 
    {
        result.push_back(developers[i] + developers[n - 1 - i]);
    }

    sort(result.begin(), result.end());

    cout << (result.back() - result.front()) << "\n";
    return 0;
}
