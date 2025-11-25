#include <iostream>
#include <vector>
using namespace std;

int main() 
{
    int N;
    cin >> N;

    vector<vector<long long>> board(N, vector<long long>(N, 0));

    for (int i = 0; i < N; i++) 
    {
        for (int j = 0; j < N; j++) 
        {
            if (i == 0 || j == 0) 
            {
                board[i][j] = 1;
            }
        }
    }

    for (int i = 1; i < N; i++) 
    {
        for (int j = 1; j < N; j++) 
        {
            board[i][j] = board[i - 1][j - 1] + board[i][j - 1] + board[i - 1][j];
        }
    }

    for (int i = 0; i < N; i++) 
    {
        for (int j = 0; j < N; j++) 
        {
            cout << board[i][j];
            if (j + 1 < N) cout << ' ';
        }
        cout << '\n';
    }

    return 0;
}
