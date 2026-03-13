#include <bits/stdc++.h>
using namespace std;

int main() 
{
    int N, B;
    cin >> N >> B;

    vector<vector<int>> gifts_info(N, vector<int>(2));
    for (int i = 0; i < N; i++) 
    {
        cin >> gifts_info[i][0] >> gifts_info[i][1];
    }

    // Please write your code here.
    int max_students = 0;

    for (int i = 0; i < N; i++) 
    {
        gifts_info[i][0] /= 2;

        vector<int> prices;
        for (int j = 0; j < N; j++) 
        {
            prices.push_back(gifts_info[j][0] + gifts_info[j][1]);
        }

        gifts_info[i][0] *= 2;

        sort(prices.begin(), prices.end());

        int students = 0;
        int cur_prices = 0;

        for (int j = 0; j < N; j++) 
        {
            if (cur_prices + prices[j] > B) 
            {
                break;
            }

            cur_prices += prices[j];
            students += 1;
        }

        max_students = max(max_students, students);
    }

    cout << max_students << '\n';
    return 0;
}