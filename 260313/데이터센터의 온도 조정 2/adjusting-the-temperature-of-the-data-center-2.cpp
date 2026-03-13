#include <bits/stdc++.h>
using namespace std;

int main() 
{
    int N, C, G, H;
    cin >> N >> C >> G >> H;

    vector<pair<int,int>> degrees(N);
    for (int i = 0; i < N; i++) 
    {
        int a, b;
        cin >> a >> b;
        degrees[i] = {a, b};
    }

    auto get_works = [&](int l, int h, int t) -> int 
    {
        if (t < l) return C;
        if (l <= t && t <= h) return G;
        return H;
    };

    int max_works = 0;
    for (int t = 0; t <= 1000; t++) 
    {
        int total = 0;
        for (auto &p : degrees) {
            total += get_works(p.first, p.second, t);
        }
        max_works = max(max_works, total);
    }

    cout << max_works << "\n";
    return 0;
}