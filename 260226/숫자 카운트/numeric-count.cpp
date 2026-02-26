#include <bits/stdc++.h>
using namespace std;

struct Ask 
{
    int d[3];  
    int cnt1;   
    int cnt2;   
};

int main() 
{
    int N;
    cin >> N;

    vector<Ask> asks;
    asks.reserve(N);

    for (int t = 0; t < N; t++) 
    {
        int num, c1, c2;
        cin >> num >> c1 >> c2;

        string s = to_string(num); 
        Ask a;
        a.d[0] = s[0] - '0';
        a.d[1] = s[1] - '0';
        a.d[2] = s[2] - '0';
        a.cnt1 = c1;
        a.cnt2 = c2;
        asks.push_back(a);
    }

    int cnts = 0;

    for (int i = 1; i <= 9; i++) 
    {
        for (int j = 1; j <= 9; j++) 
        {
            for (int k = 1; k <= 9; k++) 
            {
                if (i == j || j == k || k == i) continue;

                int pred[3] = {i, j, k};
                bool satisfied = true;

                for (const auto& ask : asks) 
                {
                    int strike = 0, ball = 0;

                    for (int l = 0; l < 3; l++) 
                    {
                        for (int n = 0; n < 3; n++) 
                        {
                            if (pred[l] == ask.d[n]) 
                            {
                                if (l == n) strike++;
                                else ball++;
                            }
                        }
                    }

                    if (strike != ask.cnt1 || ball != ask.cnt2) 
                    {
                        satisfied = false;
                        break; 
                    }
                }

                if (satisfied) cnts++;
            }
        }
    }

    cout << cnts << "\n";
    return 0;
}