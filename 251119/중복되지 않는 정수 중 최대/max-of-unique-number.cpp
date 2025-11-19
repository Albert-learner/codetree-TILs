#include <iostream>
#include <algorithm>
using namespace std;

int N, max_cst = 0;
int nums[1000];

int main() 
{
    cin >> N;
    for (int i = 0; i < N; i++) 
    {
        cin >> nums[i];
    }

    // Please write your code here.
    for(int i = 0; i < N; i++)
    {
        max_cst = max(max_cst, nums[i]);
    }
    cout << max_cst;
    return 0;
}
