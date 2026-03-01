#include <bits/stdc++.h>
using namespace std;

int main() 
{
    long long X, Y;
    cin >> X >> Y;

    int bestSum = -1;

    for (long long num = X; num <= Y; ++num) 
    {
        long long t = num;
        int s = 0;
        if (t == 0) 
        {
            s = 0;
        } 
        else 
        {
            while (t > 0) 
            {
                s += (int)(t % 10);
                t /= 10;
            }
        }
        bestSum = max(bestSum, s);
    }

    cout << bestSum << "\n";
    return 0;
}