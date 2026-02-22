#include <bits/stdc++.h>
using namespace std;

int main() 
{
    int N, K;
    cin >> N >> K;

    vector<int> candies_info(101, 0);
    for (int i = 0; i < N; i++) 
    {
        int candies, pos;
        cin >> candies >> pos;
        candies_info[pos] += candies;
    }

    // Please write your code here.
    int answer = 0;
    for (int i = 0; i < (int)candies_info.size(); i++) 
    {
        int sum = 0;
        for (int j = i - K; j <= i + K; j++) 
        {
            if (0 <= j && j < (int)candies_info.size()) 
            {
                sum += candies_info[j];
            }
        }
        answer = max(answer, sum);
    }

    cout << answer << "\n";
    return 0;
}