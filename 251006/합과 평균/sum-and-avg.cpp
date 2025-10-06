#include <iostream>
#include <iomanip>
using namespace std;

int main() 
{
    // Please write your code here.
    int a, b;
    cin >> a >> b;

    float avg = static_cast<float>(a + b) / 2;
    cout << (a + b) << ' ';
    cout << fixed << setprecision(1) << avg;
    return 0;
}