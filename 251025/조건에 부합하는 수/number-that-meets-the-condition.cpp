#include <iostream>
#include <vector>
using namespace std;

int main() 
{
    int a;
    cin >> a;

    vector<int> nums;
    for (int i = 1; i <= a; i++) 
    {
        if ((i % 2 == 1 || i % 4 == 0) && ((i / 8) % 2 != 0) && (i % 7 >= 4)) 
        {
            nums.push_back(i);
        }
    }

    for (int i = 0; i < nums.size(); i++) 
    {
        cout << nums[i];
        if (i != nums.size() - 1) cout << " ";
    }
    return 0;
}
