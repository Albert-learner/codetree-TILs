#include <iostream>
#include <vector>
using namespace std;

int main() 
{
    // Please write your code here.
    int N, M;
    cin >> N >> M;

    vector<vector<int>> board(M, vector<int>(N));
    for(int i = 0; i < N; i++)
    {
        for(int j = 1; j < M + 1; j++)
        {
            board[i][j - 1] = i * M + j;
        }
    }

    for(int i = 0; i < N; i++)
    {
        for(int j = 0; j < M; j++)
        {
            cout << board[i][j] << ' ';
        }
        cout << endl;
    }
    return 0;
}