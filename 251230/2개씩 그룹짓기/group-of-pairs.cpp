#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() 
{
    int N;
    cin >> N;

    // 실제로는 2N개의 수가 들어옴
    vector<int> n_lst(2 * N);
    for (int i = 0; i < 2 * N; i++) 
    {
        cin >> n_lst[i];
    }

    sort(n_lst.begin(), n_lst.end());

    int max_pair_sum = 0;
    for (int i = 0; i < N; i++) 
    {
        int pair_sum = n_lst[i] + n_lst[2 * N - 1 - i];
        max_pair_sum = max(max_pair_sum, pair_sum);
    }

    cout << max_pair_sum;
    return 0;
}
