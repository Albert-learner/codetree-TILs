#include <bits/stdc++.h>
using namespace std;

int main() 
{
    int N, K, P, T, t, x, y;
    cin >> N >> K >> P >> T;

    vector<array<int, 3>> handshakes(T);
    for (int i = 0; i < T; i++) 
    {
        cin >> t >> x >> y;
        handshakes[i] = {t, x, y};
    }

    // Please write your code here.
    sort(handshakes.begin(), handshakes.end(),
         [](const auto& a, const auto& b){return a[0] < b[0];});

    vector<int> people(N, 0);
    vector<int> spread(N, K);

    people[P - 1] = 1;
    for (auto &hs : handshakes) 
    {
        int x = hs[1], y = hs[2];

        bool infX = (x == P) || (people[x - 1] == 1);
        bool infY = (y == P) || (people[y - 1] == 1);

        if (infX && infY) 
        {
            spread[x - 1]--;
            spread[y - 1]--;
        } 
        else if (infX && spread[x - 1] > 0) 
        {
            people[y - 1] = 1;
            spread[x - 1]--;
        } 
        else if (infY && spread[y - 1] > 0) 
        {
            people[x - 1] = 1;
            spread[y - 1]--;
        }
    }

    for (int i = 0; i < N; i++) cout << people[i];
    cout << "\n";
    return 0;
}