#include <iostream>
#include <iomanip>
using namespace std;

int main() 
{
    // Please write your code here.
    int cst, con_sum = 0, con_cnts = 0;
    double con_avg = 0.0;
    int arr[10];

    for(int i = 0; i < 10; i++)
    {
        cin >> cst;
        arr[i] = cst;
    }

    for(int i = 0; i < 10; i++)
    {
        if(arr[i] >= 0 && arr[i] <= 200)
        {
            con_sum += arr[i];
            con_cnts += 1;
        }
    }
    con_avg = (double)con_sum / con_cnts;

    cout << fixed;
    cout << con_sum << ' ' << setprecision(1) << con_avg;
    return 0;
}