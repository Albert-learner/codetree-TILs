#include <bits/stdc++.h>
using namespace std;

int main() 
{
    // Please write your code here.
    int first, second, third;
    cin >> first >> second >> third;

    int arr[3] = {first, second, third};
    sort(arr, arr + 3);
    first = arr[0];
    second = arr[1];
    third = arr[2];

    int min_move = 0;

    while (true) 
    {
        int f_s_diff = abs(first - second);
        int s_t_diff = abs(second - third);

        if (f_s_diff == 1 && s_t_diff == 1) 
        {
            break;
        }

        if (f_s_diff == 2 || s_t_diff == 2) 
        {
            min_move += 1;
            break;
        }
        else if (f_s_diff > 2 && s_t_diff > 2) 
        {
            if (f_s_diff < s_t_diff) 
            {
                int new_second = first + 2;
                int new_third = second;
                second = new_second;
                third = new_third;
            } 
            else 
            {
                int new_first = second;
                int new_second = second + 2;
                first = new_first;
                second = new_second;
            }
        }
        else if (abs(second - third) > 2) 
        {
            int new_first = second;
            int new_second = second + 2;
            first = new_first;
            second = new_second;
        }
        else if (abs(first - second) > 2) 
        {
            int new_second = first + 2;
            int new_third = second;
            second = new_second;
            third = new_third;
        }

        min_move += 1;
    }

    cout << min_move << '\n';
    return 0;
}