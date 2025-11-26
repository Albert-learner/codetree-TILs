#include <iostream>
#include <vector>
using namespace std;

int main() 
{
    // Please write your code here.
    int N, M;
    cin >> N >> M;

    vector<vector<int>> board(N, vector<int>(N, 0));

    for(int k = 0; k < M; k++)
    {
        int x, y;
        cin >> x >> y;
        x -= 1;
        y -= 1;
        if(x >= 0 && x < N && y >= 0 && y < N)
            board[x][y] = 1;
    }

    for(int i = 0; i < N; i++)
    {
        for(int j = 0; j < N; j++)
        {
            cout << board[i][j];
            if(j + 1 < N) cout << ' ';
        }
        cout << endl;
    }
    return 0;
}