#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() 
{
    // Please write your code here.
    int n;
    cin >> n;
    vector<int> nums(n), evens;

    for(int i = 0; i < n; i++)
    {
        cin >> nums[i];
        if(nums[i] % 2 == 0)
            evens.push_back(nums[i]);
    }

    reverse(evens.begin(), evens.end());
    for(int even: evens)
        cout << even << ' ';
    return 0;
}