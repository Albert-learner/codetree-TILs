#include <bits/stdc++.h>
using namespace std;

int main() 
{
    int N;
    cin >> N;

    vector<int> n_lst(N);
    for (int i = 0; i < N; i++) 
    {
        cin >> n_lst[i];
    }

    // Please write your code here.
    long long ans = LLONG_MAX;

    for(int i = 0; i < N; i++)
    {
        long long move = 0;
        for(int j = 0; j < N; j++)
        {
            move += n_lst[j] * 1LL * llabs(j - i);
        }
        ans = min(ans, move);
    }
    cout << ans << endl;
    return 0;
}