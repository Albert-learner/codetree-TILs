#include <bits/stdc++.h>
using namespace std;

int main() 
{
    int N, M;
    cin >> N >> M;
    vector<int>bulkheads(N);
    for (int i = 0; i < N; i++) 
    {
        cin >> bulkheads[i];
    }

    // Please write your code here.
    int max_val = *max_element(bulkheads.begin(), bulkheads.end());
    int sum_val = accumulate(bulkheads.begin(), bulkheads.end(), 0);
    for(int i = max_val; i <= sum_val; i++)
    {
        vector<int>tmp;
        int total = bulkheads[0];
        for(int j = 1; j < N; j++)
        {
            if(total + bulkheads[j] > i)
            {
                tmp.push_back(total);
                total = bulkheads[j];
            }
            else
                total += bulkheads[j];
        }
        tmp.push_back(total);
        if(tmp.size() <= M)
        {
            cout << i << endl;
            break;
        }
    }
    return 0;
}