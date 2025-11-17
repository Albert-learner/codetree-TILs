#include <bits/stdc++.h>
using namespace std;

int main() 
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N, Q;
    cin >> N >> Q;

    vector<long long> n_lst(N);
    for (int i = 0; i < N; i++) 
    {
        cin >> n_lst[i];
    }

    for (int q = 0; q < Q; q++) 
    {
        int type;
        cin >> type;

        if (type == 1) 
        {
            int idx;
            cin >> idx;                
            cout << n_lst[idx - 1] << '\n';
        }
        else if (type == 2) 
        {
            long long x;
            cin >> x;
            int first_idx = 0;         
            for (int i = 0; i < N; i++) 
            {
                if (n_lst[i] == x) 
                {
                    first_idx = i + 1; 
                    break;
                }
            }
            cout << first_idx << '\n';
        }
        else 
        { 
            int l, r;
            cin >> l >> r;             
            for (int i = l - 1; i < r; i++) 
            {
                cout << n_lst[i];
                if (i + 1 < r) cout << ' ';
            }
            cout << '\n';
        }
    }

    return 0;
}
