#include <bits/stdc++.h>
using namespace std;

int main() 
{
    int N, K;
    cin >> N >> K;

    vector<int> nums(N);
    for (int i = 0; i < N; i++) 
    {
        cin >> nums[i];
    }

    int answer = -1;

    for (int i = 0; i < N; i++) 
    {
        int bomb_num = -1;

        for (int j = i + 1; j <= i + K; j++) 
        {
            if (j > N - 1) continue;

            if (nums[i] == nums[j]) 
            {
                bomb_num = nums[i];
            }
        }

        answer = max(answer, bomb_num);
    }

    cout << answer << '\n';
    return 0;
}
