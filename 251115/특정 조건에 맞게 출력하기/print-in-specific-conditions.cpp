#include <iostream>
#include <vector>
using namespace std;

int main() 
{
    vector<int> nums;
    int x;

    while (true) 
    {
        cin >> x;
        if (x == 0) break;  
        nums.push_back(x);
    }

    for (int v : nums) 
    {
        if (v % 2 == 1)
            cout << v + 3 << ' ';
        else
            cout << v / 2 << ' ';
    }

    return 0;
}
