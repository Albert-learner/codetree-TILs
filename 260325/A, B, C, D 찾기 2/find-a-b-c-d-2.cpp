#include <bits/stdc++.h>
using namespace std;

vector<int> num_lst;
unordered_set<int> num_set;

bool possible(const vector<int>& x) 
{
    int a = x[0], b = x[1], c = x[2], d = x[3];

    if (num_set.count(a + b) &&
        num_set.count(b + c) &&
        num_set.count(c + d) &&
        num_set.count(d + a) &&
        num_set.count(a + c) &&
        num_set.count(b + d) &&
        num_set.count(a + b + c) &&
        num_set.count(a + b + d) &&
        num_set.count(a + c + d) &&
        num_set.count(b + c + d) &&
        num_set.count(a + b + c + d)) 
    {
        return true;
    }

    return false;
}

int main() {
    int x;
    while (cin >> x) {
        num_lst.push_back(x);
    }

    sort(num_lst.begin(), num_lst.end());
    for (int v : num_lst) 
    {
        num_set.insert(v);
    }

    int n = (int)num_lst.size();

    for (int i = 0; i < n; i++) 
    {
        for (int j = i + 1; j < n; j++) 
        {
            for (int k = j + 1; k < n; k++) 
            {
                for (int l = k + 1; l < n; l++) 
                {
                    vector<int> comb = {num_lst[i], num_lst[j], num_lst[k], num_lst[l]};
                    if (possible(comb)) 
                    {
                        for (int num : comb) 
                        {
                            cout << num << ' ';
                        }
                        return 0;
                    }
                }
            }
        }
    }

    return 0;
}