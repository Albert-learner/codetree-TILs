#include <iostream>
#include <vector>
using namespace std;

int main() 
{
    // Please write your code here.
    int N, t_cnts = 0, t_idx = 0;
    cin >> N;
    vector<int> nums(N);

    for(int i = 0; i < N; i++)
    {
        cin >> nums[i];
        if(nums[i] == 2)
        {
            if(t_cnts != 3)
                t_cnts += 1;
            else
            {
                t_idx = i + 1;
                break;
            }
        }
    }
    cout << t_idx;
    return 0;
}