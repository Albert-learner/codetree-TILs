#include <iostream>

using namespace std;

int N;
int print_sum(int num);

int main() 
{
    cin >> N;

    // Please write your code here.
    cout << print_sum(N);
    return 0;
}

int print_sum(int num)
{
    if(num == 0 || num == 1)
        return num;

    if(num % 2 == 0)
        return num + print_sum(num - 2);
    else
        return num + print_sum(num - 2);
}