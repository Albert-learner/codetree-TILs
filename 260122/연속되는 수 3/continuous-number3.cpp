#include <bits/stdc++.h>
using namespace std;


int main() 
{
    int N;
    cin >> N;

    vector<long long> n_lst(N);
    for (int i = 0; i < N; i++) cin >> n_lst[i];

    int max_cnts = 0;
    int cur_len = 0;

    for (int i = 0; i < N; i++) 
    {
        if (i == 0 || n_lst[i] * n_lst[i - 1] < 0) 
        {
            cur_len = 1;
        } 
        else 
        {
            cur_len++;
        }
        max_cnts = max(max_cnts, cur_len);
    }

    cout << max_cnts << "\n";
    return 0;
}