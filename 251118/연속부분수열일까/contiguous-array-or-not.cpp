#include <bits/stdc++.h>
using namespace std;

int main() 
{
    int n1, n2;
    cin >> n1 >> n2;

    vector<int> a_lst(n1), b_lst(n2);
    for (int i = 0; i < n1; i++) cin >> a_lst[i];
    for (int i = 0; i < n2; i++) cin >> b_lst[i];

    if (n1 < n2) 
    {
        swap(a_lst, b_lst);
        swap(n1, n2);
    }

    bool check = false;

    for (int i = 0; i <= n1 - n2; i++) 
    {
        bool same = true;
        for (int j = 0; j < n2; j++) 
        {
            if (a_lst[i + j] != b_lst[j]) 
            {
                same = false;
                break;
            }
        }
        if (same) 
        {
            check = true;
            break;
        }
    }

    cout << (check ? "Yes" : "No") << "\n";
    return 0;
}
