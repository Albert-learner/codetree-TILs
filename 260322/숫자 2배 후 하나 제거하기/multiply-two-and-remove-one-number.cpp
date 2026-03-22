#include <bits/stdc++.h>
using namespace std;

int main() 
{
    int N;
    cin >> N;

    vector<long long> n_lst(N);
    for (int i = 0; i < N; i++) 
    {
        cin >> n_lst[i];
    }

    long long min_sum = LLONG_MAX;

    for (int i = 0; i < N; i++) 
    {
        n_lst[i] *= 2;

        for (int j = 0; j < N; j++) 
        {
            vector<long long> process_n_lst;
            process_n_lst.reserve(N - 1);

            for (int k = 0; k < N; k++) 
            {
                if (j != k) 
                {
                    process_n_lst.push_back(n_lst[k]);
                }
            }

            long long process_sum = 0;
            for (int k = 0; k < N - 2; k++) 
            {
                process_sum += llabs(process_n_lst[k + 1] - process_n_lst[k]);
            }

            min_sum = min(min_sum, process_sum);
        }

        n_lst[i] /= 2;
    }

    cout << min_sum << '\n';
    return 0;
}
