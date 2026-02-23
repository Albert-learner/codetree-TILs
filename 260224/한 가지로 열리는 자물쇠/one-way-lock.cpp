#include <bits/stdc++.h>
using namespace std;

int main() 
{
    int N, a, b, c;
    cin >> N;
    cin >> a >> b >> c;

    // Please write your code here.
    int min_comb = min({a, b, c});
    int answer = int(pow(N, 3));

    for(int i = 1; i < N + 1; i++)
    {
        for(int j = 1; j < N + 1; j++)
        {
            for(int k = 1; k < N + 1; k++)
            {
                if(abs(i - a) > 2 && abs(j - b) > 2 && abs(k - c) > 2)
                    answer -= 1;
            }
        }
    }
    cout << answer;
    return 0;
}