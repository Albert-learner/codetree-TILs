#include <bits/stdc++.h>
using namespace std;

int main() 
{
    int N;
    cin >> N;
    vector<int> A_people(N);
    vector<int> B_people(N);
    for (int i = 0; i < N; i++) 
    {
        cin >> A_people[i] >> B_people[i];
    }

    // Please write your code here.
    int min_dists = 0, dists;
    for(int i = 0; i < N; i++)
    {
        if(A_people[i] > B_people[i])
        {
            dists = A_people[i] - B_people[i];
            A_people[i] -= dists;
            A_people[i + 1] += dists;
            min_dists += dists;
        }
    }

    cout << min_dists;
    return 0;
}