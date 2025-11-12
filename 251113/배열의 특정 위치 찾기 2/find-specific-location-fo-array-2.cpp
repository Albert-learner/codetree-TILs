#include <iostream>
#include <vector>
#include <cmath>
using namespace std;

int main() 
{
    // Please write your code here.
    int odds = 0, evens = 0;
    vector<int> nums(10);

    for(int i = 0; i < 10; i++)
    {
        cin >> nums[i];
        if(i % 2 == 0)
            odds += nums[i];
        else
            evens += nums[i];
    }
    cout << abs(odds - evens);
    return 0;
}