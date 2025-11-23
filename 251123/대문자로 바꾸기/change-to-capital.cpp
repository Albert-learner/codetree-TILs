#include <iostream>
#include <vector>
#include <cctype>
using namespace std;

int main() 
{
    // Please write your code here.
    vector<vector<char>> board(5, vector<char>(3));

    for(int i = 0; i < 5; i++)
    {
        for(int j = 0; j < 3; j++)
        {
            cin >> board[i][j];
            cout << (char)toupper(board[i][j]) << ' ';
        }
        cout << endl;
    }
    return 0;
}