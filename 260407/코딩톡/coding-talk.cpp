#include <bits/stdc++.h>
using namespace std;

int main() 
{
    int n, m, p;
    cin >> n >> m >> p;

    vector<char>messages(m);
    vector<int> not_reads(m);

    for(int i = 0; i < m; i++)
        cin >> messages[i] >> not_reads[i];

    // Please write your code here.
    vector<bool> read_chk(26, false);

    for(int i = 0; i < m; i++)
    {
        if(not_reads[p - 1] == 0)
            break;

        if(i >= p - 1)
        {
            int message = messages[i] - 'A';
            read_chk[message] = true;
        }
        else if(not_reads[i] == not_reads[p - 1])
        {
            int message = messages[i] - 'A';
            read_chk[message] = true;
        }
    }

    if(not_reads[p - 1] == 0)
        cout << endl;
    else
    {
        for(int i = 0; i < n; i++)
        {
            if(!read_chk[i])
                cout << char(i + 'A') << ' ';
        }
    }
    return 0;
}