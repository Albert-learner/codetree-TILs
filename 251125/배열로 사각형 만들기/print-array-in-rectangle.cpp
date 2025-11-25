#include <iostream>
#include <vector>
using namespace std;

int main() 
{
    // Please write your code here.
    vector<vector<int>>board(5, vector<int>(5, 1));

    for(int i = 1; i < 5; i++)
    {
        for(int j = 1; j < 5; j++)
        {
            board[i][j] = board[i - 1][j] + board[i][j - 1];
        }
    }

    for(int i = 0; i < 5; i++)
    {
        for(int j = 0; j < 5; j++)
        {
            cout << board[i][j] << ' ';
        }
        cout << endl;   
    }
    return 0;
}