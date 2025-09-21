#include <iostream>
using namespace std;

int main() 
{
    // Please write your code here.
    int N, n_cnts = 0;
    cin >> N;

    for(int i = N; i < 100; i++)
    {
        if(i % N == 0 && n_cnts < 5)
        {
            cout << i << ' ';
            n_cnts += 1;
        }
        else if(i % N == 0 && n_cnts == 5)
            break;
    }
    return 0;
}