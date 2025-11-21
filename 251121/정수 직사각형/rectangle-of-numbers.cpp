#include <iostream>
#include <vector>
using namespace std;

int main() 
{
    int N, M;
    cin >> N >> M;

    vector<vector<int>> board(N, vector<int>(M));

    // 값 채우기
    for (int i = 0; i < N; i++) 
    {
        for (int j = 1; j <= M; j++) 
        {
            board[i][j - 1] = i * M + j;
        }
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
