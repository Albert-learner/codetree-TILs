#include <bits/stdc++.h>
using namespace std;

int main() 
{
    // Please write your code here.
    vector<int> nums;
    int x;

    while (cin >> x) 
    {
        nums.push_back(x);
    }

    sort(nums.begin(), nums.end());

    int a = 0, b = 0, c = 0;

    for (int i = 0; i < nums.size(); i++) 
    {
        for (int j = i + 1; j < nums.size(); j++) 
        {
            for (int k = j + 1; k < nums.size(); k++) 
            {
                if (nums[i] + nums[j] + nums[k] == nums.back()) 
                {
                    a = nums[i];
                    b = nums[j];
                    c = nums[k];
                    break;
                }
            }
        }
    }

    cout << a << ' ' << b << ' ' << c << '\n';
    return 0;
}