#include <iostream>
#include <vector>
using namespace std;

int main() 
{
    // Please write your code here.
    int n, cnts = 1;
    cin >> n;

    vector<vector<int>> grid(n);
    for(int i = 0; i < n; i++)
    {
        if(i % 2 == 0)
        {
            for(int j = 0; j < n; j++)
            {
                grid[i].push_back(cnts + j);
            }
            cnts = grid[i].back() + 2;
        }
        else
        {
            for(int j = 0; j < n * 2; j += 2)
            {
                grid[i].push_back(cnts + j);
            }
            cnts = grid[i].back() + 1;
        }
    }
    return 0;
}