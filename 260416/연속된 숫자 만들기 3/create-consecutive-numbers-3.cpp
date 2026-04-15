#include <bits/stdc++.h>
using namespace std;

int main() 
{
    // Please write your code here.
    int first, second, third;
    cin >> first >> second >> third;
    int arr[3] = {first, second, third};
    sort(arr, arr + 3);

    first = arr[0], second = arr[1], third = arr[2];

    int f_dst = abs(first - second);
    int s_dst = abs(second - third);

    int cnts = 0;
    if(f_dst == 1 && s_dst == 1)
        cnts = 0;
    else if(f_dst <= 2 && s_dst <= 2)
        cnts = 1;
    else
        cnts = max(f_dst, s_dst) - 1;

    cout << cnts;
    return 0;
}