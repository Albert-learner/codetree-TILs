#include <bits/stdc++.h>
using namespace std;

int main() 
{
    // Please write your code here.
    int ans = 0, odd = 0, even = 0;
    int N;
    cin >> N;
    vector<int> numbers(N);
    for(int i = 0; i < N; i++)
        cin >> numbers[i];

    for(int i = 0; i < N; i++)
    {
        if(numbers[i] % 2 != 0)
            odd += 1;
        else
            even += 1;
    }

    if(even > odd)
        ans = odd * 2 + 1;
    else if(even == odd)
        ans = even + odd;
    else
    {
        ans = even * 2;
        int size = odd - even;

        if(size % 3 == 0)
            ans += (int)(size / 3) * 2;
        else
        {
            if((size % 3) % 2 == 0)
                ans += (int)(size / 3) * 2 + 1;
            else
                ans += (int)(size / 3) * 2 - 1;
        }
    }
    cout << ans;
    return 0;
}
