#include <iostream>
#include <vector>
using namespace std;

int main() 
{
    // Please write your code here.
    int n, m, cst;
    cin >> n >> m;
    vector<int> nums(n);

    for(int i = 0; i < n; i++)
    {
        cin >> cst;
        nums[cst - 1] += 1;
    }

    cout << nums[m - 1];
    return 0;
}