#include <iostream>
#include <vector>
using namespace std;

int main() 
{
    int N, M;
    cin >> N >> M;

    vector<vector<int>> board(N, vector<int>(M));
    int num = 0;

    for (int j = 0; j < M; j++) 
    {
        if (j % 2 == 0) 
        {             
            for (int i = 0; i < N; i++) 
            {
                board[i][j] = num;
                num++;
            }
        } 
        else 
        {                      
            for (int i = N - 1; i >= 0; i--) 
            {
                board[i][j] = num;
                num++;
            }
        }
    }

    for (int i = 0; i < N; i++) 
    {
        for (int j = 0; j < M; j++) 
        {
            cout << board[i][j];
            if (j + 1 < M) cout << ' ';
        }
        cout << '\n';
    }

    return 0;
}
