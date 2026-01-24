#include <bits/stdc++.h>
using namespace std;

int main() 
{
    int N;
    long long T;
    cin >> N >> T;

    vector<long long> n_lst(N);
    for (int i = 0; i < N; i++) cin >> n_lst[i];

    int answer = 0, cnts = 0;
    for (int i = 0; i < N; i++) 
    {
        long long n_new = n_lst[i];
        if (n_new > T) cnts++;
        else cnts = 0;

        answer = max(answer, cnts);
    }

    cout << answer << "\n";
    return 0;
}