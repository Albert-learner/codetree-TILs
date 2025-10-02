#include <iostream>
#include <iomanip>
using namespace std;

int main() 
{
    // Please write your code here.
    float a, b;
    char c;

    cin >> c;
    cin >> a;
    cin >> b;

    cout << c << endl;
    cout << fixed << setprecision(2) << a << endl;
    cout << fixed << setprecision(2) << b << endl;
    return 0;
}