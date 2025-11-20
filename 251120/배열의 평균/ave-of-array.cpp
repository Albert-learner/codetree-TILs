#include <iostream>
#include <vector>
#include <iomanip>   
using namespace std;

int main() 
{
    vector<vector<int>> nums(2);
    int x;

    while (cin.peek() != '\n' && cin >> x) 
    {
        nums[0].push_back(x);
    }
    cin.clear(); cin.ignore(10000, '\n');

    while (cin >> x) 
    {
        nums[1].push_back(x);
    }

    int n = nums[0].size(); 

    for (int r = 0; r < 2; r++) 
    {
        double sum_row = 0;
        for (int c = 0; c < n; c++)
            sum_row += nums[r][c];
        cout << fixed << setprecision(1) << (sum_row / n) << " ";
    }
    cout << "\n";

    for (int c = 0; c < n; c++) 
    {
        double col_sum = 0;
        for (int r = 0; r < 2; r++)
            col_sum += nums[r][c];
        cout << fixed << setprecision(1) << (col_sum / 2) << " ";
    }
    cout << "\n";

    double total = 0;
    int cnt = 0;
    for (int r = 0; r < 2; r++)
        for (int c = 0; c < n; c++)
            total += nums[r][c], cnt++;

    cout << fixed << setprecision(1) << (total / cnt) << "\n";

    return 0;
}
