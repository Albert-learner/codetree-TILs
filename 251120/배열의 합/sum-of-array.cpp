#include <iostream>
#include <vector>
using namespace std;

int main() 
{
    // Please write your code here.
    int row_sum = 0;
    vector<vector<int>> arr(4, vector<int>(4));

    for(int i = 0; i < 4; i++)
    {
        for(int j = 0; j < 4; j++)
        {
            cin >> arr[i][j];
            row_sum += arr[i][j];
        }
        cout << row_sum << endl;
        row_sum = 0;
    }
    return 0;
}