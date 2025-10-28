#include <iostream>
#include <vector>
using namespace std;

int main() 
{
    // Please write your code here.
    vector<int> nums(5);
    for(int i = 0; i < 5; i++)
    {
        cin >> nums[i];
    }

    bool allDivisibleBy3 = true;
    for(int n: nums)
    {
        if(n % 3 != 0)
        {
            allDivisibleBy3 = false;
            break;
        }
    }

    cout << (allDivisibleBy3 ? 1 : 0);
    return 0;
}