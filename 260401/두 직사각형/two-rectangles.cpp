#include <bits/stdc++.h>
using namespace std;

int main() 
{
    int x1, y1, x2, y2;
    int a1, b1, a2, b2;

    cin >> x1 >> y1 >> x2 >> y2;
    cin >> a1 >> b1 >> a2 >> b2;

    vector<vector<int>> board(101, vector<int>(101, 0));

    for (int i = x1; i <= x2; i++) 
    {
        for (int j = y1; j <= y2; j++) 
        {
            board[i][j] += 1;
        }
    }

    // Please write your code here.
    for (int i = a1; i <= a2; i++) 
    {
        for (int j = b1; j <= b2; j++) 
        {
            board[i][j] += 1;
        }
    }

    bool confirm = false;
    for (int i = 0; i < 101; i++) 
    {
        for (int j = 0; j < 101; j++) 
        {
            if (board[i][j] >= 2) 
            {
                confirm = true;
                break;
            }
        }
        if (confirm) break;
    }

    if (confirm) 
    {
        cout << "overlapping\n";
    } 
    else 
    {
        cout << "nonoverlapping\n";
    }
    return 0;
}