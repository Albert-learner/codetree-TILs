#include <iostream>
using namespace std;

int main() 
{
    // Please write your code here.
    int n, n_sum = 0, stop_i = 0;
    cin >> n;

    for(int i = 1; i <= 100; i++)
    {
        n_sum += i;
        if(n_sum >= n)
        {
            stop_i = i;
            break;
        }
    }
    cout << stop_i;
    return 0;
}