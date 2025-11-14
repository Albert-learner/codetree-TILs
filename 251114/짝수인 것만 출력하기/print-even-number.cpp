#include <iostream>
#include <vector>
using namespace std;

int main() 
{
    // Please write your code here.
    int n;
    cin >> n;
    vector<int> nums(n);

    for(int i = 0; i < n; i++)
    {
        cin >> nums[i];
    }

    for(int i = 0; i < n; i++)
    {
        if(nums[i] % 2 == 0)
            cout << nums[i] << ' ';
    }
    return 0;
}