#include <iostream>
#include <vector>
using namespace std;

int main() 
{
    // Please write your code here.
    vector<int> nums(10);
    for(int i = 0; i < 10; i++)
    {
        cin >> nums[i];
    }

    cout << nums[2] + nums[4] + nums[9];
    return 0;
}