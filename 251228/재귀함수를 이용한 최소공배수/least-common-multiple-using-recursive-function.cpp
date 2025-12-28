#include <iostream>
#include <vector>
using namespace std;

vector<long long> n_lst;

long long GCD(long long a, long long b) 
{
    if (a % b == 0) 
    {
        return b;
    }
    return GCD(b, a % b);
}

long long LCM(int n) 
{
    if (n == 0) 
    {
        return n_lst[0];
    } 
    else if (n == 1) 
    {
        return (n_lst[0] * n_lst[1]) / GCD(n_lst[0], n_lst[1]);
    }

    long long prev = LCM(n - 1);
    return (prev * n_lst[n]) / GCD(prev, n_lst[n]);
}

int main() 
{
    int N;
    cin >> N;

    n_lst.resize(N);
    for (int i = 0; i < N; i++) 
    {
        cin >> n_lst[i];
    }

    cout << LCM(N - 1);
    return 0;
}
