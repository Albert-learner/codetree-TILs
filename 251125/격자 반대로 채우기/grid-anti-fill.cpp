#include <iostream>
#include <vector>
using namespace std;

int main() 
{
    // Please write your code here.
    int N, num = 0;
    cin >> N;
    vector<vector<int>>board(N, vector<int>(N, 0));

    if(N % 2 == 0)
    {
        for(int j = N - 1; ㅓ > -1; j--)
        {
            if(j % 2 == 1)
            {
                for(int i = N - 1, i > -1; i--)
                {
                    num += 1;
                    board[i][j] = num;
                }
            }
            else
            {
                for(int i = 0; i < N; i++)
                {
                    num += 1;
                    board[i][j] = num;
                }
            }
        }
    }
    else
    {
        for(int j = N - 1; j > -1; j--)
        {           
            if(j % 2 == 0)
            {
                for(int i = N - 1; i > -1; i--)
                {
                    num += 1;
                    board[i][j] = num;
                }
            }
            else{
                for(int i = 0; i < N; i++)
                {
                    num += 1;
                    board[i][j] = num;
                }
            }
        }
    }
    return 0;
}