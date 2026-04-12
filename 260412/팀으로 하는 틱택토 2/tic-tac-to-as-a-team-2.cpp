#include <bits/stdc++.h>
using namespace std;

int main() 
{
    // Please write your code here.
    vector<vector<int>> board(3, vector<int>(3));

    for (int i = 0; i < 3; i++) 
    {
        string s;
        cin >> s;
        for (int j = 0; j < 3; j++) 
        {
            board[i][j] = s[j] - '0';
        }
    }

    set<pair<int, int>> teams;

    for (int i = 0; i < 3; i++) 
    {
        set<int> chk;
        for (int j = 0; j < 3; j++) 
        {
            chk.insert(board[i][j]);
        }
        if (chk.size() == 2) 
        {
            auto it = chk.begin();
            int a = *it;
            ++it;
            int b = *it;
            teams.insert({min(a, b), max(a, b)});
        }
    }

    for (int j = 0; j < 3; j++) 
    {
        set<int> chk;
        for (int i = 0; i < 3; i++) 
        {
            chk.insert(board[i][j]);
        }
        if (chk.size() == 2) 
        {
            auto it = chk.begin();
            int a = *it;
            ++it;
            int b = *it;
            teams.insert({min(a, b), max(a, b)});
        }
    }

    {
        set<int> chk;
        for (int i = 0; i < 3; i++) 
        {
            chk.insert(board[i][i]);
        }
        if (chk.size() == 2) 
        {
            auto it = chk.begin();
            int a = *it;
            ++it;
            int b = *it;
            teams.insert({min(a, b), max(a, b)});
        }
    }
    {
        set<int> chk;
        for (int i = 0; i < 3; i++) 
        {
            chk.insert(board[i][2 - i]);
        }
        if (chk.size() == 2) {
            auto it = chk.begin();
            int a = *it;
            ++it;
            int b = *it;
            teams.insert({min(a, b), max(a, b)});
        }
    }

    cout << teams.size() << '\n';
    return 0;
}