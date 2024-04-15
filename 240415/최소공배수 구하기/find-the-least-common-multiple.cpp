#include <iostream>
using namespace std;

int GCD(int n, int m)
{
    if (n < m)
        swap(n, m);

    while (m > 0)
    {
        int tmp = m;
        m = n % m;
        n = tmp;
    }

    return n;
}

int main() {
    int N, M;
    cin >> N >> M;

    int gcd = GCD(N, M);
    cout << N * M / gcd;
    return 0;
}