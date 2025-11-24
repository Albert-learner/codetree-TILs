#include <iostream>
#include <vector>
using namespace std;

int main() 
{
    int N, M;
    cin >> N >> M;

    vector<vector<int>> board(N, vector<int>(M, 0));

    int num = 1;
    int ij_sum = 0;

    while (ij_sum <= N * M) 
    {
        for (int i = 0; i < N; i++) 
        {
            for (int j = 0; j < M; j++) 
            {
                if (i + j == ij_sum) 
                {
                    board[i][j] = num;
                    num++;
                }
            }
        }
        ij_sum++;
        if (num > N * M) break;   
    }

    for (int i = 0; i < N; i++) 
    {
        for (int j = 0; j < M; j++) 
        {
            cout << board[i][j];
            if (j + 1 < M) cout << " ";
        }
        cout << "\n";
    }

    return 0;
}
