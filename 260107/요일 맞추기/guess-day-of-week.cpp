#include <bits/stdc++.h>
using namespace std;

int main() 
{
    int m1, d1, m2, d2, start_date = 0, end_date = 0;
    cin >> m1 >> d1 >> m2 >> d2;

    // Please write your code here.
    vector<pair<int,int>> month_days = {
        {1, 31}, {2, 28}, {3, 31}, {4, 30}, {5, 31}, {6, 30}, 
        {7, 31}, {8, 31}, {9, 30}, {10, 31}, {11, 30}, {12, 31}  
    };

    for (auto &md : month_days) 
    {
        int month = md.first, days = md.second;
        if (month <= m1 - 1) start_date += days;
        if (month <= m2 - 1) end_date += days;
    }
    start_date += d1;
    end_date += d2;

    vector<string> day_name = {"Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"};
    int diff = end_date - start_date;
    int idx = ((diff % 7) + 7) % 7;

    cout << day_name[idx];
    return 0;
}