#include <iostream>
#include <vector>
using namespace std;

int main() 
{
    int a, b;
    cin >> a >> b;
    vector<int> nums(10);
    nums[0] = a;
    nums[1] = b;
    for(int i = 2; i < 10; i++)
    {
        nums[i] = (nums[i - 2] + nums[i - 1]) % 10;   
    }

    for(int i = 0; i < 10; i++)
    {
        cout << nums[i] << ' ';
    }
    return 0;
}
