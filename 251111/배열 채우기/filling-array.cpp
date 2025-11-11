#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() 
{
    // Please write your code here.
    int cst;
    vector<int> nums(10);
    for(int i = 0; i < 10; i++)
    {
        cin >> cst;
        if(cst != 0)
            nums[i] = cst;
        else
            break;
    }

    reverse(nums.begin(), nums.end());
    for(int num:nums)
    {
        if(num != 0)
            cout << num << ' ';
    }
    return 0;
}