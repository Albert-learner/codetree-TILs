#include <iostream>
#include <vector>
using namespace std;

int main() 
{
    // Please write your code here.
    vector<int> nums(10);
    for(int i = 0; i < 10;i++)
    {
        cin >> nums[i];
        if(nums[i] % 3 == 0)
        {
            cout << nums[i - 1];
            break;
        }
    }
    return 0;
}