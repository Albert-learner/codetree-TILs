#include <iostream>
#include <cmath>
using namespace std;

int a, b;
bool is_prime_number(int x);

int main() 
{
    cin >> a >> b;

    // Please write your code here.
    if(a == 1 && b == 1)
        cout << 0;
    else
    {
        int prime_sum = 0;
        for(int i = a; i < b + 1; i++)
        {
            if(is_prime_number(i))
                prime_sum += i;
        }
        cout << prime_sum;
    }
    return 0;
}

bool is_prime_number(int x)
{
    for(int i = 2; i < int(pow(x, 0.5)) + 1; i++)
    {
        if(x % i == 0)
            return false;
    }

    return true;
}