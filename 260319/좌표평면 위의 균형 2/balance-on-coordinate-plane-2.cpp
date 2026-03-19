#include <bits/stdc++.h>
using namespace std;

int main() 
{
    int N;
    cin >> N;

    vector<pair<int, int>> points(N);
    vector<int> x_lst(N), y_lst(N);

    for (int i = 0; i < N; i++) 
    {
        int x, y;
        cin >> x >> y;
        points[i] = {x, y};
        x_lst[i] = x;
        y_lst[i] = y;
    }

    // Please write your code here.
    int min_cnts = INT_MAX;

    for (int i = 0; i <= 100; i++) 
    {
        if (i % 2 == 1) continue;

        for (int j = 0; j <= 100; j++) 
        {
            if (j % 2 == 1) continue;

            int n1 = 0, n2 = 0, n3 = 0, n4 = 0;

            for (int k = 0; k < N; k++) 
            {
                if (x_lst[k] < i && y_lst[k] > j) 
                {
                    n1++;
                } 
                else if (x_lst[k] > i && y_lst[k] > j) 
                {
                    n2++;
                } 
                else if (x_lst[k] > i && y_lst[k] < j) 
                {
                    n3++;
                } 
                else 
                {
                    n4++;
                }
            }

            int max_cnt = max({n1, n2, n3, n4});
            min_cnts = min(min_cnts, max_cnt);
        }
    }

    cout << min_cnts << '\n';
    return 0;
}