#include <iostream>
#include <vector>
using namespace std;

int main() 
{
    vector<int> nums;
    int x;

    while (cin >> x) 
    {
        if (x == 0) break;
        nums.push_back(x);
    }

    vector<int> tens_cntr(10, 0); 

    for (int num : nums) 
    {
        if (num >= 10) 
        {
            int first_digit = num;
            while (first_digit >= 10) 
            {
                first_digit /= 10;   
            }
            if (1 <= first_digit && first_digit <= 9) 
            {
                tens_cntr[first_digit]++;
            }
        }
    }

    for (int d = 1; d <= 9; d++) 
    {
        cout << d << " - " << tens_cntr[d] << '\n';
    }

    return 0;
}
