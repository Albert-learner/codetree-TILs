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
        cout << nums[i] * nums[i] << ' ';
    }
    return 0;
}