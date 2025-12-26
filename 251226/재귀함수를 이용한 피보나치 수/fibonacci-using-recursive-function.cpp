#include <iostream>

using namespace std;

int N;
int fibonacci(int num);

int main() 
{
    cin >> N;

    // Please write your code here.
    cout << fibonacci(N);
    return 0;
}

int fibonacci(int num)
{
    if(num == 1 || num == 2)
        return 1;

    return fibonacci(num - 1) + fibonacci(num - 2);
}