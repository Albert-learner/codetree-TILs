#include <bits/stdc++.h>
using namespace std;

int main() 
{
    int N, K;
    cin >> N >> K;

    vector<int> n_lst(N);
    for (int i = 0; i < N; i++) 
    {
        cin >> n_lst[i];
    }

    sort(n_lst.begin(), n_lst.end());

    // Please write your code here.
    int max_cnts = 0;

    for (int i = 0; i < N; i++) 
    {
        int cnts = 1;
        for (int j = i + 1; j < N; j++) 
        {
            if (abs(n_lst[j] - n_lst[i]) <= K) 
            {
                cnts++;
            } 
            else 
            {
                break;
            }
        }
        max_cnts = max(max_cnts, cnts);
    }

    cout << max_cnts << '\n';
    return 0;
}
