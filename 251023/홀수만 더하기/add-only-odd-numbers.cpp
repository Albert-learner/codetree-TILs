#include <iostream>
#include <vector>
using namespace std;

int main() 
{
    // Please write your code here.
    int n, cst, c_sum = 0;
    vector<int> nums;
    cin >> n;

    for(int i = 0; i < n; i++)
    {
        cin >> cst;
        if(cst % 2 == 1 && cst % 3 == 0)
            c_sum += cst;
    }
    cout << c_sum;
    return 0;
}