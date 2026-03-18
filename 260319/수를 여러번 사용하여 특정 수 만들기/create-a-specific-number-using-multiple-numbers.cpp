#include <bits/stdc++.h>
using namespace std;

int main() 
{
    int A, B, C;
    cin >> A >> B >> C;

    // Please write your code here.
    int max_result = 0, cnt, num_b;
    for(int i = 0; i < (int)(C / A) + 1; i++)
    {
        cnt = A * i;
        num_b = (C - cnt) / B;
        cnt += num_b * B;
        max_result = max(max_result, cnt);
    }

    cout << max_result;
    return 0;
}