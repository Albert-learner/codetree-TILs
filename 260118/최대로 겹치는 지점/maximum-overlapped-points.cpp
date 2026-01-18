#include <bits/stdc++.h>
using namespace std;

int main() 
{
    int N, start, end;
    cin >> N;

    vector<int> checked(100);
    for (int i = 0; i < N; i++) 
    {
        cin >> start >> end;
        for(int i = start; i < end + 1; i++)
        {
            checked[i - 1] += 1;
        }
    }

    // Please write your code here.
    cout << *max_element(checked.begin(), checked.end());
    return 0;
}