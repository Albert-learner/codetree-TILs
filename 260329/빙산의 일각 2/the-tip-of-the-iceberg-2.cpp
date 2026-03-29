#include <bits/stdc++.h>
using namespace std;

int main() 
{
    int N;
    cin >> N;

    vector<int>ice_bergs(N, 0);
    for (int i = 0; i < N; i++) 
    {
        cin >> ice_bergs[i];
    }

    // Please write your code here.
    int max_height = *max_element(ice_bergs.begin(), ice_bergs.end());
    int max_cnts = 0;

    for(int i = 0; i < max_height; i++)
    {
        vector<int> tmp_ice_bergs(ice_bergs.begin(), ice_bergs.begin() + N);

        for (int j = 0; j < N; j++) 
        {
            if (tmp_ice_bergs[j] - i < 0) 
            {
                tmp_ice_bergs[j] = 0;
            } 
            else 
            {
                tmp_ice_bergs[j] -= i;
            }
        }

        int cnts = 0, bit = 0;
        for (int chk = 0; chk < N; chk++) 
        {
            if (tmp_ice_bergs[chk] != 0) 
            {
                bit = 1;
            }

            if (bit == 1 && tmp_ice_bergs[chk] == 0) 
            {
                bit = 0;
                cnts += 1;
            }

            if (bit == 1 && chk == N - 1) 
            {
                cnts += 1;
            }
        }

        max_cnts = max(max_cnts, cnts);
    }
    cout << max_cnts;
    return 0;
}
