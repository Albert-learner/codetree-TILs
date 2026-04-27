#include <bits/stdc++.h>
using namespace std;

int main() 
{
    // Please write your code here.
    int N;
    cin >> N;
    vector<long long> n_lst(N);
    for(int i = 0; i < N; i++)
        cin >> n_lst[i];

    sort(n_lst.begin(), n_lst.end());

    long long max_multiply = n_lst[N - 1] * n_lst[N - 2] * n_lst[N - 3];

    max_multiply = max(max_multiply, n_lst[0] * n_lst[1] * n_lst[N - 1]);

    cout << max_multiply << '\n';
    return 0;
}