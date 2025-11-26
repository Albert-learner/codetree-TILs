#include <iostream>
#include <vector>
using namespace std;

int main() 
{
    // Please write your code here.
    int N, M;
    cin >> N >> M;

    vector<vector<long long>> board(N, vector<long long>(N, 0));

    for (int k = 0; k < M; k++) 
    {
        long long x, y;
        cin >> x >> y;
        int r = x - 1;  
        int c = y - 1;  
        if (r >= 0 && r < N && c >= 0 && c < N) 
            board[r][c] = x * y;
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