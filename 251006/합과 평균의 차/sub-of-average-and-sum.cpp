#include <iostream>
using namespace std;

int main() 
{
    // Please write your code here.
    int a, b, c;
    cin >> a >> b >> c;

    float avg = static_cast<float>(a + b + c) / 3;
    cout << a + b + c << endl;
    cout << avg << endl;
    cout << (a + b + c) - avg;

    return 0;
}