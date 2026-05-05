#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() 
{
    vector<int> nums;
    int x;

    while (cin >> x) 
    {
        nums.push_back(x);
    }

    sort(nums.begin(), nums.end());

    int a = 0, b = 0, c = 0, d = 0;

    for (int i = 0; i < nums.size(); i++) 
    {
        for (int j = i + 1; j < nums.size(); j++) 
        {
            for (int k = j + 1; k < nums.size(); k++) 
            {
                for (int l = k + 1; l < nums.size(); l++) 
                {
                    if (nums[i] <= nums[j] &&
                        nums[j] <= nums[k] &&
                        nums[k] <= nums[l] &&
                        nums[k] <= nums[i] + nums[j] &&
                        nums[i] + nums[j] + nums[k] + nums[l] == nums.back()) 
                        {
                        
                        a = nums[i];
                        b = nums[j];
                        c = nums[k];
                        d = nums[l];
                    }
                }
            }
        }
    }

    cout << a << ' ' << b << ' ' << c << ' ' << d << '\n';

    return 0;
}