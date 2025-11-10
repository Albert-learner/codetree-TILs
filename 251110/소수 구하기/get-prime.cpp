#include <iostream>
#include <vector>
#include <cmath>
using namespace std;

bool is_prime_number(int n) 
{
    if (n < 2) 
        return false;
    for (int i = 2; i <= sqrt(n); i++) 
    {
        if (n % i == 0)
            return false;
    }
    return true;
}

int main() 
{
    int N;
    cin >> N;

    vector<int> prime_numbers;
    for (int i = 2; i <= N; i++) 
    {
        if (is_prime_number(i))
            prime_numbers.push_back(i);
    }

    for (size_t i = 0; i < prime_numbers.size(); i++) 
    {
        cout << prime_numbers[i];
        if (i + 1 < prime_numbers.size()) 
            cout << ' ';
    }
    cout << '\n';

    return 0;
}
