#include <iostream>
#include <algorithm>
using namespace std;

int n, max_profit = 0, min_price, profit;
int price[1000];

int main() 
{
    cin >> n;
    for (int i = 0; i < n; i++) 
    {
        cin >> price[i];
    }

    // Please write your code here.
    min_price = price[0];
    for(int i = 0; i < n; i++)
    {
        profit = price[i] - min_price;

        if(profit > max_profit)
            max_profit = profit;

        if(min_price > price[i])
            min_price = price[i];
    }

    cout << max_profit;
    return 0;
}
