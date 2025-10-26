#include <iostream>
using namespace std;

int main() 
{
    // Please write your code here.
    int n, i_cst = 0, n_mul = 1;
    cin >> n;

    for(int i = 1; i <= 10; i++)
    {
        n_mul *= i;
        if(n_mul >= n)
        {
            i_cst = i;
            break;
        }
    }
    cout << i_cst;
    return 0;
}