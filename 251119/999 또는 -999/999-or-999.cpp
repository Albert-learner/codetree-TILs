#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() 
{
    // Please write your code here.
    int min_cst = 999, max_cst = 0;
    vector<int> nums(100);

    for(int i = 0; i < 100; i++)
    {
        cin >> nums[i];
        if(nums[i] == 999 || nums[i] == -999)
        {
            nums[i] = 0;
            break;
        }
        min_cst = min(min_cst, nums[i]);
        max_cst = max(max_cst, num[i]);
    }

    cout << max_cst << ' ' << min_cst;
    return 0;
}