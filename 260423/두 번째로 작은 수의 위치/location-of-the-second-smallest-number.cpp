#include <bits/stdc++.h>
using namespace std;

int main() 
{
    // Please write your code here.
    int N;
    cin >> N;
    vector<int> n_lst(N);
    for(int i = 0; i < N; i++)
    {
        cin >> n_lst[i];
    }

    vector<int> uniq_n_lst = n_lst;
    sort(uniq_n_lst.begin(), uniq_n_lst.end());
    uniq_n_lst.erase(unique(uniq_n_lst.begin(), uniq_n_lst.end()), uniq_n_lst.end());

    if (uniq_n_lst.size() == 1) 
    {
        cout << -1 << '\n';
    } 
    else 
    {
        int target = uniq_n_lst[1];

        int cnt = 0;
        int idx = -1;

        for (int i = 0; i < N; i++) 
        {
            if (n_lst[i] == target) 
            {
                cnt++;
                if (idx == -1) idx = i;
            }
        }

        if (cnt > 1) 
        {
            cout << -1 << '\n';
        } 
        else if (cnt == 1) 
        {
            cout << idx + 1 << '\n';  
        }
    }

    return 0;
}
