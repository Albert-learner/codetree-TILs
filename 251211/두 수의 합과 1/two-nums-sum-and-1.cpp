#include <iostream>
#include <string>

using namespace std;

int main() 
{
    // Please write your code here.
    int first, second, nums_sum = 0, one_cnts = 0;
    string sum_str = "";
    cin >> first >> second;

    nums_sum = first + second;
    sum_str = to_string(nums_sum);
    for(int i = 0; i < sum_str.size(); i++)
    {
        if(sum_str[i] == '1')
            one_cnts += 1;
    }
    cout << one_cnts;
    return 0;
}