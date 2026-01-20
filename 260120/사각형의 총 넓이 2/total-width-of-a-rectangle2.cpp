#include <bits/stdc++.h>
using namespace std;

int main() 
{
    int N, x1, x2, y1, y2;
    cin >> N;
    vector<vector<int>>arr(201, vector<int>(201, 0));

    for (int i = 0; i < N; i++) 
    {
        cin >> x1 >> y1 >> x2 >> y2;
        x1 += 100;
        y1 += 100;
        x2 += 100;
        y2 += 100;

        for(int r = x1; r < x2; r++)
        {
            for(int c = y1; c < y2; c++)
                arr[r][c] = 1;
        }
    }

    // Please write your code here.
    long long cnts = 0;
    for(int r = 0; r < 201; r++)
    {
        for(int c = 0; c < 201; c++)
            if(arr[r][c] == 1) cnts += 1;
    }

    cout << cnts << endl;
    return 0;
}