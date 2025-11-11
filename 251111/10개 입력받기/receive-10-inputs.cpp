#include <iostream>
#include <vector>
#include <iomanip>
#include <numeric>
using namespace std;

int main() 
{
    // Please write your code here.
    int cst, nums_sum = 0, zeros = 0;
    double avg = 0.0;
    vector<int> nums(10);
    for(int i = 0; i < 10; i++)
    {
        cin >> cst;
        if(cst != 0)
        {
            nums[i] = cst;
            zeros += 1;            
        }
        else
            break;
    }

    nums_sum = accumulate(nums.begin(), nums.end(), 0);
    avg = (double)nums_sum / zeros;

    cout << nums_sum << ' ';
    cout << fixed << setprecision(1) << avg;
    return 0;
}