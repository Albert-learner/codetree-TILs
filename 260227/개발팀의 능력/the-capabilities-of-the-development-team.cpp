#include <bits/stdc++.h>
using namespace std;

long long get_diff(const vector<long long>& dev, long long total, int i, int j, int k, int w) 
{
    long long sum1 = dev[i] + dev[j];
    long long sum2 = dev[k] + dev[w];
    long long sum3 = total - (sum1 + sum2);

    if (sum1 == sum2 || sum2 == sum3 || sum3 == sum1) return -1;

    long long result = llabs(sum1 - sum2);
    result = max(result, llabs(sum1 - sum3));
    result = max(result, llabs(sum2 - sum3));
    return result;
}

int main() 
{
     vector<long long> developers(5);
    for (int i = 0; i < 5; i++) cin >> developers[i];

    long long total = 0;
    for (auto v : developers) total += v;

    long long min_cst = 1000001;
    bool flag = true;

    for (int i = 0; i < 5; i++) 
    {
        for (int j = i + 1; j < 5; j++) 
        {
            for (int k = 0; k < 5; k++) 
            {
                for (int w = k + 1; w < 5; w++) 
                {
                    if (i == k || i == w || j == k || j == w) continue;

                    long long diff = get_diff(developers, total, i, j, k, w);
                    if (diff != -1) 
                    {
                        min_cst = min(min_cst, diff);
                        flag = false;
                    }
                }
            }
        }
    }

    if (flag) cout << -1 << '\n';
    else cout << min_cst << '\n';
    return 0;
}