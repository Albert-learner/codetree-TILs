#include <bits/stdc++.h>
using namespace std;

int n;
int x[1000];
char dir[1000];

int main() 
{
    int N;
    cin >> N;

    vector<int> colored(200001, 0);
    int cur_pos = 100000;

    for (int t = 0; t < N; t++) 
    {
        int size;
        char mv_dir;
        cin >> size >> mv_dir;

        if (mv_dir == 'R') 
        {
            for (int i = cur_pos; i < cur_pos + size; i++) 
            {
                colored[i] = 1;
            }
            cur_pos += size - 1;
        } 
        else 
        { 
            for (int i = cur_pos; i > cur_pos - size; i--) 
            {
                colored[i] = 2;
            }
            cur_pos -= size - 1;
        }
    }

    long long cnt2 = 0, cnt1 = 0;
    for (int v : colored) 
    {
        if (v == 2) cnt2++;
        else if (v == 1) cnt1++;
    }

    cout << cnt2 << " " << cnt1 << "\n";
    return 0;
}