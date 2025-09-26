#include <iostream>
#include <cmath>
using namespace std;

int main() 
{
    // Please write your code here.
    float a = 25.352;

    cout << fixed;
    cout.precision(1);
    cout << round(a * 10) / 10;
    return 0;
}