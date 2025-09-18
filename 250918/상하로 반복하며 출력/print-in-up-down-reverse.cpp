#include <iostream>
using namespace std;

int main() {
    // Please write your code here.
    int N, ini, n_sum = 0;
    cin >> N;

    n_sum = N + 1;
    for(int i = 1; i <= N; i++)
    {
        ini = i;
        for(int j = 1; j <= N; j++)
        {
            cout << ini;
            ini = n_sum - ini;
        }
        cout << endl;
    }
    return 0;
}