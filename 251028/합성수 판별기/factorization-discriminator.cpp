#include <iostream>
using namespace std;

int main() 
{
    // Please write your code here.
    int n, c_nums = 0;
    cin >> n;

    for(int i = 2; i <= n - 1; i++)
    {
        if(n % i == 0)
        {
            c_nums += 1;
            cout << "C";
            break;
        }
    }

    if(c_nums == 0)
        cout << "N";
    return 0;
}