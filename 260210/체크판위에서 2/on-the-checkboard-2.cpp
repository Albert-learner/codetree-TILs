#include <bits/stdc++.h>
using namespace std;

struct State
{
    int cnt;
    int r;
    int c;
    string val;
};

int main() 
{
    int R, C;
    cin >> R >> C;

    vector<vector<string>> board(R, vector<string>(C));
    for (int i = 0; i < R; i++) 
    {
        for (int j = 0; j < C; j++) 
        {
            cin >> board[i][j];
        }
    }

    // Please write your code here.
    long long answer = 0;
    vector<State> st;
    st.push_back({0, 0, 0, board[0][0]});

    while(!st.empty())
    {
        State cur = st.back();
        st.pop_back();

        int cnt = cur.cnt;
        int r = cur.r;
        int c = cur.c;

        if(r == R - 1 && c == C - 1 && cnt == 3)
        {
            answer += 1;
            continue;
        }

        for (int mr = r + 1; mr < R; mr++) 
        {
            for (int mc = c + 1; mc < C; mc++) 
            {
                if (board[r][c] != board[mr][mc]) 
                {
                    st.push_back({cnt + 1, mr, mc, board[mr][mc]});
                }
            }
        }
    }

    cout << answer;
    return 0;
}