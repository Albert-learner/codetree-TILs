#include <iostream>
#include <vector>
using namespace std;

int main() 
{
    // Please write your code here.
    int a1, a2;
    vector<int> nums(10);
    cin >> a1 >> a2;

    nums[0] = a1;
    nums[1] = a2;
    for(int i = 2; i < 10; i++)
    {
        nums[i] = nums[i - 1] + 2 * nums[i - 2];
    }

    for(int num: nums)
    {
        cout << num << ' ';
    }
    return 0;
}