#include <bits/stdc++.h>
using namespace std;

pair<long long, vector<string>> bubble_sort(vector<string> lst)
{
    long long cnts = 0;
    for(int i = lst.size() - 1; i > 0; i--)
    {
        for(int j = 0; j < i; j++)
        {
            if(lst[j] > lst[j + 1])
            {
                swap(lst[j], lst[j + 1]);
                cnts += 1;
            }
        }
    }
    return {cnts, lst};
}

int main() 
{
    // Please write your code here.
    int N;
    cin >> N;
    
    vector<string> line(N);
    for(int i = 0; i < N; i++)
        cin >> line[i];

    auto result = bubble_sort(line);
    long long total_cnts = result.first;

    cout << total_cnts;
    return 0;
}