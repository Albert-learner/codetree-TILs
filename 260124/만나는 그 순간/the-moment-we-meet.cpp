#include <bits/stdc++.h>
using namespace std;

int n, m;
char d[1000];
int t[1000];
char d2[1000];
int t2[1000];

int main() 
{
    int N, M;
    cin >> N >> M;

    vector<pair<char,int>> n_moves(N), m_moves(M);
    for (int i = 0; i < N; i++) 
    {
        char dir; int size;
        cin >> dir >> size;
        n_moves[i] = {dir, size};
    }
    for (int i = 0; i < M; i++) 
    {
        char dir; int size;
        cin >> dir >> size;
        m_moves[i] = {dir, size};
    }
    // Please write your code here.
    vector<long long> a, b;
    a.reserve(2000000);
    b.reserve(2000000);

    long long cur_a = 0, cur_b = 0;

    a.push_back(cur_a);
    for (auto [dir, size] : n_moves) 
    {
        if (dir == 'R') 
        {
            for (int step = 0; step < size; step++) 
            {
                cur_a += 1;
                a.push_back(cur_a);
            }
        } 
        else 
        { 
            for (int step = 0; step < size; step++) 
            {
                cur_a -= 1;
                a.push_back(cur_a);
            }
        }
    }

    b.push_back(cur_b);
    for (auto [dir, size] : m_moves) 
    {
        if (dir == 'R') 
        {
            for (int step = 0; step < size; step++) 
            {
                cur_b += 1;
                b.push_back(cur_b);
            }
        } 
        else 
        {
            for (int step = 0; step < size; step++) 
            {
                cur_b -= 1;
                b.push_back(cur_b);
            }
        }
    }

    int T = min((int)a.size(), (int)b.size()) - 1;
    int answer = -1;

    for (int t = 1; t <= T; t++) 
    { 
        if (a[t] == b[t]) 
        {
            answer = t;
            break;
        }
    }

    cout << answer << "\n";

    return 0;
}