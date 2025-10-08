#include <iostream>
using namespace std;

int main() 
{
    // Please write your code here.
    int a, b;
    cin >> a >> b;

    b = a < b ? b : a;
    cout << b;
    return 0;
}