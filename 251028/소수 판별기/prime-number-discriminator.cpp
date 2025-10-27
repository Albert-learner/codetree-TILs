#include <iostream>
#include <cmath>
using namespace std;

bool is_prime_number(int num)
{
    for(int i = 2; i <= int(pow(num, 0.5)) + 1; i++)
    {
        if(num % i == 0)
            return false;
    }

    return true;
}

int main() 
{
    // Please write your code here.
    int n;
    cin >> n;

    if(is_prime_number(n))
        cout << "P";
    else
        cout << "C";

    return 0;
}