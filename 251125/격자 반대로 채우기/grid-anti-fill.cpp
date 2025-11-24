#include <iostream>
#include <vector>
using namespace std;

int main() {
    int N;
    cin >> N;

    vector<vector<int>> board(N, vector<int>(N, 0));

    int num = 0;

    if (N % 2 == 0) 
    {
        for (int j = N - 1; j >= 0; --j) 
        {
            if (j % 2 == 1) 
            {                
                for (int i = N - 1; i >= 0; --i) 
                {
                    num++;
                    board[i][j] = num;
                }
            } 
            else 
            {
                for (int i = 0; i < N; ++i) 
                {
                    num++;
                    board[i][j] = num;
                }
            }
        }
    } 
    else 
    {
        for (int j = N - 1; j >= 0; --j) 
        {
            if (j % 2 == 0) 
            {
                for (int i = N - 1; i >= 0; --i) 
                {
                    num++;
                    board[i][j] = num;
                }
            } 
            else 
            {
                for (int i = 0; i < N; ++i) 
                {
                    num++;
                    board[i][j] = num;
                }
            }
        }
    }

    for (int i = 0; i < N; ++i) 
    {
        for (int j = 0; j < N; ++j) 
        {
            cout << board[i][j];
            if (j + 1 < N) cout << ' ';
        }
        cout << '\n';
    }

    return 0;
}
