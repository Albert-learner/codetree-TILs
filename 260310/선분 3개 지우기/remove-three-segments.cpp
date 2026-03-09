#include <bits/stdc++.h>
using namespace std;

int main() 
{
    int N;
    cin >> N;

    vector<pair<int, int>> lines(N);
    for (int i = 0; i < N; i++) 
    {
        cin >> lines[i].first >> lines[i].second;
    }

    int cases = 0;

    for (int i = 0; i < N; i++) 
    {
        for (int j = i + 1; j < N; j++) 
        {
            for (int k = j + 1; k < N; k++) 
            {

                vector<int> confirm_lines(100, 0);
                bool flag = true;

                for (int l = 0; l < N; l++) 
                {
                    if (l == i || l == j || l == k) continue;

                    for (int m = lines[l].first; m <= lines[l].second; m++) 
                    {
                        confirm_lines[m] += 1;
                        if (confirm_lines[m] > 1) 
                        {
                            flag = false;
                        }
                    }
                }

                if (flag) 
                {
                    cases += 1;
                }
            }
        }
    }

    cout << cases << '\n';
    return 0;
}
