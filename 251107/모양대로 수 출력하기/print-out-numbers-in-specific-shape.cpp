#include <iostream>
using namespace std;

int main() 
{
    int N;
    cin >> N;

    for (int i = 0; i < N; i++) 
    {
        for (int s = 0; s < 2 * i; s++) 
        {
            cout << ' ';
        }

 
        for (int j = N - i; j >= 1; j--) 
        {
            cout << j << ' ';
        }

        cout << '\n';
    }

    return 0;
}
