#include <bits/stdc++.h>
using namespace std;

int main() 
{
    int N, L;
    cin >> N >> L;
    vector<int>seqs(N);

    for (int i = 0; i < N; i++) 
    {
        cin >> seqs[i];
    }

    // Please write your code here.
    for(int H = N; H >= 0; H--)
    {
        int l_cnt = 0, h_cnt = 0;
        for(int i = 0; i < N; i++)
        {
            if(seqs[i] >= H)
            {
                h_cnt += 1;
            }
            else if(seqs[i] == H - 1)
            {
                h_cnt += 1;
                l_cnt += 1;
            }
        }

        if(h_cnt >= H && (l_cnt - (h_cnt - H)) <= L)
        {
            cout << H << "\n";
            break;
        }
    }
    return 0;
}