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

    cout << n << endl;
    return n;
}

int main() {
    int N, M;
    int gcd_cst = 0;
    cin >> N >> M;

    GCD(N, M);

    return 0;
}