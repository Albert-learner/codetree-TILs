#include <iostream>
#include <vector>
using namespace std;

int main() 
{
    // Please write your code here.
    int two_cnts = 0, two_sum = 0, cst;
    vector<int>nums(10);

    for(int i = 0; i < 10; i++)
    {
        cin >> cst;
        if(cst != 0)
        {
            nums[i] = cst;
            if(cst % 2 == 0)
            {
                two_cnts += 1;
                two_sum += cst;
            }   
        }
        else
            break; 
    }
    cout << two_cnts << ' ' << two_sum;
    return 0;
}