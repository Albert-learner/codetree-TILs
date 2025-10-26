#include <iostream>
#include <vector>
using namespace std;

int main() 
{
    // Please write your code here.
    int n;
    vector<int> nums;
    cin >> n;

    while(n != 0)
    {
        nums.push_back(n);
        cin >> n;
    }

    for(int i = 0; i < nums.size(); i++)
    {
        cout << nums[i] << endl;
    }
    return 0;
}