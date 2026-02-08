#include <bits/stdc++.h>
using namespace std;


int main() 
{
    int N;
    cin >> N;

    vector<string> board(N);
    for (int i = 0; i < N; i++) 
    {
        cin >> board[i];
    }

    long long K;
    cin >> K;

    // Please write your code here.
    int dx[4] = {1, 0, -1, 0};
    int dy[4] = {0, -1, 0, 1};

    int slash_dir[4] = {1, 0, 3, 2};
    int rev_slash_dir[4] = {3, 2, 1, 0};

    int dir = 0;
    long long r = 0, c = 0;

    if (K <= N) 
    {
        dir = 0;
        r = 0; c = K - 1;
    } 
    else if (N < K && K <= 2LL * N) 
    {
        dir = 1;
        r = K - N - 1; c = N - 1;
    } 
    else if (2LL * N < K && K <= 3LL * N) 
    {
        dir = 2;
        r = N - 1; c = 3LL * N - K;
    } 
    else 
    { 
        dir = 3;
        r = 4LL * N - K; c = 0;
    }

    long long cnts = 0;
    while (0 <= r && r < N && 0 <= c && c < N) 
    {
        if (board[(int)r][(int)c] == '/') 
        {
            dir = slash_dir[dir];
        } 
        else if (board[(int)r][(int)c] == '\\') 
        {
            dir = rev_slash_dir[dir];
        }

        r += dx[dir];
        c += dy[dir];
        cnts++;
    }

    cout << cnts << "\n";
    return 0;
}
