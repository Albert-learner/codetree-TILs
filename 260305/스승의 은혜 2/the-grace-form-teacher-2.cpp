#include <bits/stdc++.h>
using namespace std;

int main() 
{
    int N, B;
    cin >> N >> B;

    vector<int> prices(N);
    for (int i = 0; i < N; i++) 
    {
        cin >> prices[i];
    }

    // Please write your code here.
    sort(prices.begin(), prices.end());
    int max_cnts = 0, cnts, satisfy, price;
    for(int i = 0; i < N; i++)
    {
        cnts = 0;
        satisfy = B;
        for(int j = 0; j < N; j++)
        {
            if(j == i)
                price = prices[j] / 2;
            else
                price = prices[j];
            
            if(satisfy >= price)
            {
                satisfy -= price;
                cnts += 1;
            }
        }
        max_cnts = max(max_cnts, cnts);
    }

    cout << max_cnts;
    return 0;
}