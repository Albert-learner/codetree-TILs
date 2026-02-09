#include <bits/stdc++.h>
using namespace std;


int main() 
{
    int N;
    cin >> N;
    vector<int> cows(N);
    for (int i = 0; i < N; i++) 
    {
        cin >> cows[i];
    }

    // Please write your code here.
    int answer = 0;
    for(int i = 0; i < cows.size(); i++)
    {
        for(int j = i + 1; j < cows.size(); j++)
        {
            for(int k = j + 1; k < cows.size(); k++)
            {
                if(cows[i] <= cows[j] && cows[j] <= cows[k])
                    answer += 1;
            }
        }
    }

    cout << answer;
    return 0;
}