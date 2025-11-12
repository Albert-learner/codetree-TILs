#include <iostream>
#include <vector>
using namespace std;

int main() 
{
    vector<int> n_lst;
    int x;

    while (cin >> x) 
        n_lst.push_back(x);

    vector<int> zero_idxs;
    for (int i = 0; i < (int)n_lst.size(); i++) 
        if (n_lst[i] == 0) 
            zero_idxs.push_back(i);

    int z = zero_idxs[0];

    int sum_val = 0;
    for (int i = z - 3; i < z; i++) 
        sum_val += n_lst[i];

    cout << sum_val << endl;
    return 0;
}
