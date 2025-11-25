#include <iostream>
#include <vector>
using namespace std;

int main() 
{
    // Please write your code here.
    int N;
    cin >> N;
    vector<vector<int>> board(N, vector<int>(N, 0));

    for(int i = 1; i < N; i++)
    {
        for(int j = 1; j < N; j++)
        {
            board[i][j] = board[i - 1][j - 1] + board[i][j - 1] + board[i - 1][j]
        }
    }

    for(int i = 0; i < N; i++)
    {
        for(int j = 0; j < N; j++)
        {
            cout << board[i][j] << ' ';
        }
        cout << endl;
    }
    return 0;
}