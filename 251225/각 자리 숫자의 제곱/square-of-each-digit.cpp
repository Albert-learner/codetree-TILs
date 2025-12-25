#include <iostream>
using namespace std;

long long power_sum(long long n) 
{
    if (n < 10) 
    {
        return n * n;
    }
    return power_sum(n / 10) + (n % 10) * (n % 10);
}

int main() 
{
    long long N;
    cin >> N;

    cout << power_sum(N);
    return 0;
}
