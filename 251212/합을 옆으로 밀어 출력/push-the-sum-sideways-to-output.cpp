#include <iostream>
#include <vector>
#include <string>
#include <numeric>
using namespace std;

int main() 
{
    // Please write your code here.
    int N, cst, n_sum = 0;
    vector<int> nums;
    string n_sum_str = "";
    char first_chr;
    cin >> N;

    for(int i = 0; i < N; i++)
    {
        cin >> cst;
        nums.push_back(cst);
    }

    n_sum = accumulate(nums.begin(), nums.end(), 0);
    n_sum_str = to_string(n_sum);
    first_chr = n_sum_str[0];
    cout << n_sum_str.substr(1) + first_chr;
    return 0;
}