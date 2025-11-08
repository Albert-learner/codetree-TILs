#include <iostream>
using namespace std;

int main() 
{
    // Please write your code here.
    int n, nums;
    cin >> n;

    nums = n;
    for(int i = 1; i < n + 1; i++)
    {
        for(int j = 1; j < nums + 1; j++)
        {
            if(j == nums)
                cout << i << " * " << j << " = " << i * j << endl;
            else
                cout << i << " * " << j << " = " << i * j << " / ";

        }
        nums -= 1;
    }
    return 0;
}