#include <bits/stdc++.h>
using namespace std;

int N;
vector<char> seats;

int get_dist() 
{
    int min_num = 2100000000;
    int last_flag = -1, cur_flag = -1;

    for (int i = 0; i < N; i++) 
    {
        char cur_chr = seats[i];
        if (cur_chr == '1') 
        {
            cur_flag = i;
        } 
        else 
        {
            cur_flag = -1;
        }

        if (cur_flag != -1) 
        {
            if (last_flag != -1) 
            {
                int sub = cur_flag - last_flag;
                min_num = min(min_num, sub);
            }
            last_flag = cur_flag;
        }
    }

    return min_num;
}

int main() 
{
    cin >> N;
    string s;
    cin >> s;
    seats.assign(s.begin(), s.end());

    // Please write your code here.
    int max_dist = 0;

    for (int i = 0; i < N; i++) 
    {
        for (int j = i + 1; j < N; j++) 
        {
            if (seats[i] == '1' || seats[j] == '1') 
            {
                continue;
            }

            seats[i] = '1';
            seats[j] = '1';

            max_dist = max(max_dist, get_dist());

            seats[i] = '0';
            seats[j] = '0';
        }
    }

    cout << max_dist << '\n';
    return 0;
}