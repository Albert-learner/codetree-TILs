#include <iostream>
#include <iomanip>
using namespace std;

int main() 
{
    // Please write your code here.
    int n, cst, n_sum = 0, n_cnts = 0;
    double avg = 0.0;
    cin >> n;
    int nums[n];

    for(int i = 0; i < n; i++)
    {
        cin >> cst;
        nums[i] = cst;
        n_sum += cst;
    }
    avg = double(n_sum) / n;
    cout << fixed;
    cout << n_sum << ' ' << setprecision(1) << avg;
    return 0;
}