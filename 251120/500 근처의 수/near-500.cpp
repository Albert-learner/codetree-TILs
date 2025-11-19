#include <iostream>
#include <vector>
#include <limits>
using namespace std;

int main() 
{
    vector<int> nums;
    int x;
    while (cin >> x) 
        nums.push_back(x);

    int max_lower = numeric_limits<int>::min();  
    int min_over  = numeric_limits<int>::max();  

    for (int num : nums) 
    {
        if (num < 500) 
        {
            if (num > max_lower) 
                max_lower = num;
        } 
        else if (num > 500) 
        {
            if (num < min_over) 
                min_over = num;
        }
    }

    cout << max_lower << " " << min_over << '\n';
    return 0;
}
