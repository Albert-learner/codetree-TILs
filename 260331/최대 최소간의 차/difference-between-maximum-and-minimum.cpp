#include <bits/stdc++.h>
using namespace std;

int main() 
{
    int N, K;
    cin >> N >> K;

    const int MAX_N = 100;
    vector<int> n_lst;
    n_lst.reserve(MAX_N);

    for (int i = 0; i < N; i++) 
    {
        int x;
        cin >> x;
        n_lst.push_back(x);
    }

    // Please write your code here.
    while ((int)n_lst.size() < MAX_N) 
    {
        n_lst.push_back(0);
    }

    int cst = 0;

    while (true) 
    {
        int cur_min = 10000;
        int cur_max = 1;
        int min_idx = 0, max_idx = 0;

        for (int i = 0; i < N; i++) 
        {
            if (cur_min > n_lst[i]) 
            {
                cur_min = n_lst[i];
                min_idx = i;
            }
            if (cur_max < n_lst[i])
            {
                cur_max = n_lst[i];
                max_idx = i;
            }
        }

        int min_cnts = 0, max_cnts = 0;
        for (int i = 0; i < N; i++) 
        {
            if (n_lst[i] == cur_min) min_cnts++;
            if (n_lst[i] == cur_max) max_cnts++;
        }

        if (cur_max - cur_min <= K) 
        {
            break;
        } 
        else 
        {
            if (min_cnts >= max_cnts) 
            {
                n_lst[max_idx] -= 1;
                cst += 1;
            } 
            else 
            {
                n_lst[min_idx] += 1;
                cst += 1;
            }
        }
    }

    cout << cst << '\n';
    return 0;
}