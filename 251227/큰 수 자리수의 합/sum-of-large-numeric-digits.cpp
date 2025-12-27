#include <iostream>

using namespace std;

int a, b, c;
int add_all(int total);

int main() 
{
    cin >> a >> b >> c;

    // Please write your code here.
    int mul_three = a * b * c;

    cout << add_all(mul_three);
    return 0;
}

int add_all(int total)
{
    if(total < 10)
        return total;

    return add_all((int)(total / 10)) + total % 10;
}