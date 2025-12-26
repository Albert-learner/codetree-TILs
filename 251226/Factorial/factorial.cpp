#include <iostream>

using namespace std;

int N;
int factorial(int num);

int main() 
{
    cin >> N;

    // Please write your code here.
    cout << factorial(N);
    return 0;
}

int factorial(int num)
{
    if(num == 0 || num == 1)
        return 1;

    return num * factorial(num - 1);
}