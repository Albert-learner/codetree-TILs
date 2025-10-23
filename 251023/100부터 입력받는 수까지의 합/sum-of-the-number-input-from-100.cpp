#include <iostream>
using namespace std;

int main() 
{
    // Please write your code here.
    int n, total_sum = 0;
    cin >> n;

    for(int i = n; i <= 100; i++)
    {
        total_sum += i;
    }
    cout << total_sum;
    return 0;
}