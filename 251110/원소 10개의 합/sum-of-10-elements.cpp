#include <iostream>
#include <vector>
#include <numeric>
using namespace std;

int main() 
{
    // Please write your code here.
    vector<int> nums(10);
    for(int i = 0; i < 10; i++)
    {
        cin >> nums[i];
    }

    int vec_sum = accumulate(nums.begin(), nums.end(), 0);
    cout << vec_sum;
    return 0;
}