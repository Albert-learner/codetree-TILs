#include <bits/stdc++.h>
using namespace std;

int main() 
{
    int N, M;
    cin >> N >> M;
    vector<int> a(N), b(M);
    for (int i = 0; i < N; i++) cin >> a[i];
    for (int i = 0; i < M; i++) cin >> b[i];

    // Please write your code here.
    unordered_map<int, int> need;
    need.reserve(M * 2);
    for (int x : b) need[x]++;

    int haveKinds = 0;                 
    int totalKinds = (int)need.size(); 
    unordered_map<int, int> window;
    window.reserve(M * 2);

    for (int i = 0; i < M; i++) 
    {
        int x = a[i];
        auto it = need.find(x);
        if (it != need.end()) 
        {
            int before = window[x];
            window[x] = before + 1;
            if (before + 1 == it->second) haveKinds++; 
        }
    }

    long long answer = 0;
    if (haveKinds == totalKinds) answer++;

    for (int i = M; i < N; i++) 
    {
        int out = a[i - M];
        auto itOutNeed = need.find(out);
        if (itOutNeed != need.end()) 
        {
            int before = window[out];
            if (before == itOutNeed->second) haveKinds--; 
            if (--window[out] == 0) window.erase(out);
        }

        int in = a[i];
        auto itInNeed = need.find(in);
        if (itInNeed != need.end()) 
        {
            int before = window[in];
            window[in] = before + 1;
            if (before + 1 == itInNeed->second) haveKinds++;
        }

        if (haveKinds == totalKinds) answer++;
    }

    cout << answer << "\n";
    return 0;
}