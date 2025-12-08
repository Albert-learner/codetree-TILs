#include <iostream>
using namespace std;

int main() 
{
    // Please write your code here.
    char first, second;
    int ch_sum = 0, ch_diff = 0;
    cin >> first >> second;

    ch_sum = (int)first + (int)second;
    ch_diff = abs((int)first - (int)second);

    cout << ch_sum << ' ' << ch_diff;
    return 0;
}