#include <iostream>
#include <iomanip>
#include <cmath>
using namespace std;

int main() 
{
    // Please write your code here.
    int a, b, fs_sum = 0, fs_cnts = 0;
    float fs_avg = 0.0;
    cin >> a >> b;

    for(int i = a; i <= b; i++)
    {
        if(i % 5 == 0 || i % 7 == 0)
        {
            fs_sum += i;
            fs_cnts += 1;
        }
    }

    fs_avg = round(10 * fs_sum / fs_cnts) / 10;
    cout << fixed;
    cout << fs_sum << ' ' << setprecision(1) << fs_avg;
    return 0;
}