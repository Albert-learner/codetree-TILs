#include <iostream>
#include <cmath>
using namespace std;

int main() 
{
    // Please write your code here.
    float feet = 30.48;
    double mile = 160934;

    cout << fixed;
    cout.precision(1);
    cout << "9.2ft = " << round(9.2 * feet * 10) / 10 << "cm" << endl;
    cout << "1.3mi = " << round(1.3 * mile * 10) / 10 << "cm"; 
    return 0;
}