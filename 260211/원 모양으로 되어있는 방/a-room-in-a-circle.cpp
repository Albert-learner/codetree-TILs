#include <bits/stdc++.h>
using namespace std;


int main() 
{
    int N;
    cin >> N;
    vector<long long> people(N);
    for (int i = 0; i < N; i++) cin >> people[i];

    // Please write your code here.
    long long MIN_DST = LLONG_MAX;

    for (int i = 0; i < N; i++) 
    {
        long long sum_dst = 0;
        for (int j = 0; j < N; j++) 
        {
            long long dst = (j + N - i) % N;
            sum_dst += dst * people[j];
        }
        MIN_DST = min(MIN_DST, sum_dst);
    }

    cout << MIN_DST << "\n";

    return 0;
}