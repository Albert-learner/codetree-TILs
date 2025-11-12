#include <iostream>
#include <vector>
#include <iomanip>
using namespace std;

int main() 
{
    // Please write your code here.
    int e_idxs = 0, t_idxs = 0, threes = 0;
    vector<int> nums(10);
    for(int i = 0; i < 10; i++)
    {
        cin >> nums[i];
        if(i % 2 == 1)
            e_idxs += nums[i];
        else if((i + 1) % 3 == 0)
        {
            t_idxs += nums[i];
            threes += 1;
        } 
    }

    cout << e_idxs << ' ';
    cout << fixed << setprecision(1) << (double)t_idxs / threes;'
    return 0;
}