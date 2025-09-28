#include <iostream>
using namespace std;

int main() 
{
    // Please write your code here.
    int a = 1, b = 2, c = 3, tmp;
    tmp = a + b + c;
    a = tmp;
    b = tmp;
    c = tmp;

    cout << a << ' ' << b << ' ' << c;
    return 0;
}