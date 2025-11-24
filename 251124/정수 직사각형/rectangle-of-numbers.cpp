#include <iostream>
using namespace std;

int main() 
{
    // Please write your code here.
    int N, M, cost = 1;
    cin >> N >> M;

    for(int i = 0; i < N; i++)
    {
        for(int j = 0; j < M; j++)
        {
            cout << cost << ' ';
            cost += 1;
        }
        cout << endl;
    }
    return 0;
}