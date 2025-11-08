#include <iostream>
using namespace std;

int main() 
{
    int N;
    cin >> N;

    char start_chr = 'A';
    for (int i = 0; i < N; i++) 
    {
        for (int j = 0; j < N; j++) 
        {
            cout << char(start_chr + i * N + j);
        }
        cout << '\n';
    }

    return 0;
}
