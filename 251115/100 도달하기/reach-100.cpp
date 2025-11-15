#include <iostream>
#include <vector>
using namespace std;

int main() 
{
    int n;
    cin >> n;

    vector<int> nums;
    nums.push_back(1);
    nums.push_back(n);

    cout << nums[0] << ' ' << nums[1] << ' ';

    int idx = 2;

    while (true) 
    {
        int nextVal = nums[idx - 2] + nums[idx - 1];
        nums.push_back(nextVal);
        cout << nextVal << ' '; 

        if (nextVal > 100) 
            break;

        idx++;
    }

    return 0;
}
