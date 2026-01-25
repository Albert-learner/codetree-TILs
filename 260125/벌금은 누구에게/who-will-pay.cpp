#include <bits/stdc++.h>
using namespace std;

int N, M, K;
int student[10000];

int main()
{
    int N, M, K;
    cin >> N >> M >> K;

    vector<int> cnt(N + 1, 0);

    int answer = -1;
    for (int i = 0; i < M; i++) 
    {
        int penalty;
        cin >> penalty;

        if (1 <= penalty && penalty <= N) 
        {
            cnt[penalty]++;

            if (cnt[penalty] >= K) 
            {
                answer = penalty;
                for (int j = i + 1; j < M; j++) 
                {
                    int tmp; cin >> tmp;
                }
                break;
            }
        }
    }

    cout << answer << "\n";
    return 0;
}