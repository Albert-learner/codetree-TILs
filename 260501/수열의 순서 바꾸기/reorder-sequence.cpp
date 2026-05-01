#include <bits/stdc++.h>
using namespace std;

int main() 
{
    // Please write your code here.
    int N;
    cin >> N;
    vector<int>n_lst(N);

    for(int i = 0; i < N; i++)
        cin >> n_lst[i];

    int cnts = 0;
    for(int i = 0; i < N; i++)
    {
        bool flag = false;
        for(int j = i; j < N - 1; j++)
        {
            if(n_lst[j] > n_lst[j + 1])
                flag = true;
        }
        if(flag)
            cnts += 1;
    }

    cout << cnts;
    return 0;
}
