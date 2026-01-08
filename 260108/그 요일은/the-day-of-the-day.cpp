#include <bits/stdc++.h>
using namespace std;

int main() 
{
    int m1, m2, d1, d2;
    string find_day;
    cin >> m1 >> d1 >> m2 >> d2;
    cin >> find_day;

    // Please write your code here.
    vector<string> days = {"Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"};
    vector<int> months = {0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};

    auto get_num = [&](const string& f_day) -> int{
        for(int i = 0; i < 7; i++)
            if(days[i] == f_day) 
                return i;

        return 0;
    };

    int day_num = get_num(find_day);
    d1 += day_num;

    auto total_days = [&](int m, int d) -> long long{
        long long t_days = 0;
        for (int i = 1; i < m; i++) t_days += months[i];
        t_days += d;
        return t_days;
    };

    long long diff_days = total_days(m2, d2) - total_days(m1, d1);
    
    if(diff_days < 0)
        cout << 0 << endl;
    else
        cout << (diff_days / 7 + 1) << "\n";
    return 0;
}