#include <iostream>
using namespace std;

long long recur_seq(long long num);

int main() 
{
    long long N;
    cin >> N;

    cout << recur_seq(N);
    return 0;
}

long long recur_seq(long long n) 
{
    if (n == 1) 
    {
        return 0;
    }

    if (n % 2 == 0) 
    {
        return recur_seq(n / 2) + 1;
    } 
    else 
    {
        return recur_seq(n * 3 + 1) + 1;
    }
}