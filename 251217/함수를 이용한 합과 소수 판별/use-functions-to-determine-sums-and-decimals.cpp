#include <iostream>
#include <cmath>
using namespace std;

int a, b;
bool is_prime_number(int num);
int digit_sum(int x);

int main() 
{
    int i_sum = 0, cnts = 0;
    cin >> a >> b;

    // Please write your code here.
    for(int i = a; i < b + 1; i++)
    {
        if(is_prime_number(i))
        {
            i_sum = digit_sum(i);
            if(i_sum % 2 == 0)
                cnts += 1;
        }
    }

    cout << cnts;
    return 0;
}

bool is_prime_number(int num)
{
    for(int i = 2; i < (int)pow(num, 0.5) + 1; i++)
    {
        if(num % i == 0)
            return false;
    }

    return true;
}

int digit_sum(int x)
{
    int s = 0;
    while(x > 0)
    {
        s += x % 10;
        x /= 10;
    }

    return s;
}