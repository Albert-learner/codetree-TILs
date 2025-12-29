#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() 
{
    int N, k;
    cin >> N >> k;
    vector<int>nums(N);

    for (int i = 0; i < N; i++) 
    {
        cin >> nums[i];
    }

    // Please write your code here.
    sort(nums.begin(), nums.end());
    cout << nums[k - 1];
    return 0;
}
