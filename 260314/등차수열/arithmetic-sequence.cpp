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
    sort(n_lst.begin(), n_lst.end());

    int max_cnts = 0;

    for (int num = 1; num <= 100; num++) 
    {
        int cnts = 0;

        for (int i = 0; i < N; i++) 
        {
            for (int j = i + 1; j < N; j++) 
            {
                if ((n_lst[i] + n_lst[j]) / 2.0 == num) 
                {
                    cnts += 1;
                }
            }
        }

        max_cnts = max(max_cnts, cnts);
    }

    cout << max_cnts << '\n';
    return 0;
}