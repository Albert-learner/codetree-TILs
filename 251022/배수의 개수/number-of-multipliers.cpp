#include <iostream>
#include <vector>
using namespace std;

int main() 
{
    // Please write your code here.
    int threes = 0, fives = 0, cst;
    vector<int> nums(10);

    for(int i = 0; i < 10; i++)
    {
        cin >> cst;
        nums[i] = cst;
    }

    for(int i = 0; i < 10; i++)
    {
        if(nums[i] % 3 == 0)
            threes += 1;
        
        if(nums[i] % 5 == 0)
            fives += 1;
    }
    cout << threes << ' ' << fives;

    return 0;
}