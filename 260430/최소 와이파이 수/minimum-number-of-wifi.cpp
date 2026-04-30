#include <bits/stdc++.h>
using namespace std;

int N, M;
vector<int> people;

int new_idx(int n_idx) 
{
    for (int i = 0; i < N; i++) 
    {
        if (i >= n_idx && people[i] == 1) 
        {
            return i;
        } 
        else if (i == N - 1) 
        {
            return n_idx;
        } 
        else 
        {
            continue;
        }
    }
    return n_idx;
}

bool is_range(int x) 
{
    if (x >= N) 
    {
        return false;
    } 
    else if (people[x] == 0) 
    {
        return true;
    } 
    else 
    {
        return false;
    }
}

int count_one(int l, int r) 
{
    int cnt = 0;
    r = min(r, N);

    for (int i = l; i < r; i++) 
    {
        if (people[i] == 1) 
        {
            cnt++;
        }
    }

    return cnt;
}

int main() 
{
    // Please write your code here.
    cin >> N >> M;

    people.resize(N);
    for (int i = 0; i < N; i++) 
    {
        cin >> people[i];
    }

    int cnts = 0;

    bool has_one = false;
    for (int x : people) 
    {
        if (x == 1) 
        {
            has_one = true;
            break;
        }
    }

    if (!has_one) 
    {
        cout << cnts << '\n';
    } 
    else 
    {
        int idx = 0;

        while (idx < N) 
        {
            int ones = count_one(idx, idx + 2 * M + 1);

            if (ones != 0) 
            {
                cnts++;
            }

            if (ones == 0 || is_range(idx + 2 * M + 1)) 
            {
                int now_idx = idx + 2 * M + 1;
                idx = new_idx(now_idx);
            } 
            else 
            {
                idx += 2 * M + 1;
            }
        }
        cout << cnts << '\n';
    }
    return 0;
}
