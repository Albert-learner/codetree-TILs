#include <iostream>
#include <vector>
using namespace std;

int main() 
{
    int N, num = 0;
    cin >> N;

    vector<vector<int>> board(N, vector<int>(N, 0));

    for (int i = 0; i < N; i++) 
    {
        for (int j = 0; j < N; j++) 
        {
            num += 1;
            board[j][i] = num;   
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
