#include <iostream>
using namespace std;

int main() 
{
    // Please write your code here.
    int a, b, c, d, start_time = 0, end_time = 0;
    cin >> a >> b >> c >> d;

    start_time = a * 60 + b;
    end_time = c * 60 + d;

    cout << end_time - start_time;
    return 0;
}
