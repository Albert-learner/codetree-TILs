#include <iostream>
#include <vector>
#include <numeric>
using namespace std;

int main() {
    int N, N_cpy;
    cin >> N;

    N_cpy = N;
    vector <int> nums;
    while (N_cpy > 0)
    {
        nums.insert(nums.begin(), N_cpy % 10);
        N_cpy /= 10;
    }

    if (N % 2 == 0 and accumulate(nums.begin(), nums.end(), 0) % 5 == 0)
        cout << "Yes";
    else
        cout << "No";

    return 0;
}