#include <iostream>
using namespace std;

int main() 
{
    int a, b, c, start_time = 0, end_time = 0;
    cin >> a >> b >> c;

    // Please write your code here.
    start_time = 10 * 24 * 60 + 11 * 60 + 11;
    end_time = (a - 1) * 24 * 60 + b * 60 + c;

    if(end_time - start_time < 0)
        cout << -1;
    else
        cout << end_time - start_time;
    return 0;
}
