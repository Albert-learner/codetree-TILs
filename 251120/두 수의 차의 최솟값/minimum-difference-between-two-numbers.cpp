#include <iostream>
#include <vector>
using namespace std;

int main() 
{
    // Please write your code here.
    int N, min_diff, diff;
    cin >> N;
    vector<int> n_lst(N);

    for(int i = 0; i < N; i++)
        cin >> n_lst[i];

    min_diff = n_lst[N - 1] - n_lst[0];
    for(int i = 0; i < N; i++)
    {
        for(int j = i + 1; j < N; j++)
        {
            diff = n_lst[j] - n_lst[i];
            if(diff < min_diff)
                min_diff = diff;
        }
    }
    cout << min_diff;
    return 0;
}