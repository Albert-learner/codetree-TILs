#include <iostream>
#include <iomanip>
using namespace std;

int main() 
{
    // Please write your code here.
    int a, b;
    cin >> a >> b;


    float result = static_cast<float>(a + b) / (a - b);
    cout << fixed << setprecision(2) << result;
    return 0;
}