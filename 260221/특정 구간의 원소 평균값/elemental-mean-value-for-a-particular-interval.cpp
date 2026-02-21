#include <bits/stdc++.h>
using namespace std;

int main() 
{
    int N;
    cin >> N;
    vector<long long> a(N);
    for (int i = 0; i < N; i++) cin >> a[i];

    // Please write your code here.
    long long answer = 0;

    for (int i = 0; i < N; i++) 
    {
        long long sum = 0;
        unordered_set<long long> seen;
        seen.reserve((size_t)(N - i) * 2);

        for (int j = i; j < N; j++) 
        {
            sum += a[j];
            seen.insert(a[j]);

            int len = j - i + 1;

            if (sum % len == 0) 
            {
                long long mean = sum / len;
                if (seen.find(mean) != seen.end()) 
                {
                    answer++;
                }
            }
        }
    }

    cout << answer << "\n";
    return 0;
}