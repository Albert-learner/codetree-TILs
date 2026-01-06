#include <bits/stdc++.h>
using namespace std;

int main() 
{
    int N;
    cin >> N;
    vector<long long> n_lst(N);
    for (int i = 0; i < N; i++) cin >> n_lst[i];

    vector<long long> sorted_lst = n_lst;
    sort(sorted_lst.begin(), sorted_lst.end());

    unordered_map<long long, vector<int>> posMap;
    posMap.reserve((size_t)N * 2);

    for (int i = 0; i < N; i++) 
    {
        posMap[sorted_lst[i]].push_back(i + 1);
    }

    unordered_map<long long, int> ptr;
    ptr.reserve((size_t)N * 2);

    vector<int> answer;
    answer.reserve(N);

    for (int i = 0; i < N; i++) 
    {
        long long v = n_lst[i];
        int &p = ptr[v];           
        answer.push_back(posMap[v][p]);
        p++;
    }

    for (int i = 0; i < N; i++) 
    {
        cout << answer[i] << (i + 1 < N ? ' ' : '\n');
    }
    return 0;
}
