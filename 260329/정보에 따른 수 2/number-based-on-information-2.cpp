#include <bits/stdc++.h>
using namespace std;

int main() 
{
    int T, a, b;
    cin >> T >> a >> b;

    vector<int> S, N;
    S.reserve(T);
    N.reserve(T);

    for (int i = 0; i < T; i++) 
    {
        char alphabet;
        int pos;
        cin >> alphabet >> pos;
        if (alphabet == 'S') S.push_back(pos);
        else if (alphabet == 'N') N.push_back(pos);
    }

    sort(S.begin(), S.end());
    sort(N.begin(), N.end());

    int s_idx = 0, n_idx = 0;
    long long nearest_cnts = 0;

    for (int cur_pos = a; cur_pos <= b; cur_pos++) 
    {
        while (s_idx < (int)S.size() - 1 &&
               llabs((long long)cur_pos - S[s_idx]) > llabs((long long)cur_pos - S[s_idx + 1])) 
        {
            s_idx++;
        }
        long long s_dst = llabs((long long)cur_pos - S[s_idx]);

        while (n_idx < (int)N.size() - 1 &&
               llabs((long long)cur_pos - N[n_idx]) > llabs((long long)cur_pos - N[n_idx + 1])) 
        {
            n_idx++;
        }
        long long n_dst = llabs((long long)cur_pos - N[n_idx]);

        if (s_dst <= n_dst) nearest_cnts++;
    }

    cout << nearest_cnts << "\n";
    return 0;
}