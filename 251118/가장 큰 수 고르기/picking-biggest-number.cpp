#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() 
{
    // Please write your code here.
    int max_cst = 0;
    vector<int> nums(10);
    for(int i = 0; i < 10; i++)
    {
        cin >> nums[i];
        max_cst = max(max_cst, nums[i]);
    }
    cout << max_cst;
    return 0;
}