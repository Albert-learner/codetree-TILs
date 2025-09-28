#include <iostream>
using namespace std;

int main() 
{
    // Please write your code here.
    int a = 5, b = 6, c = 7, tmp;

    tmp = c;
    c = b;
    b = a;
    a = tmp;

    cout << a << endl;
    cout << b << endl;
    cout << c;
    return 0;
}