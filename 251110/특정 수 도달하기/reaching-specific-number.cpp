#include <iostream>
#include <vector>
#include <iomanip>  
using namespace std;

int main() 
{
    vector<int> n_lst(10);
    for (int i = 0; i < 10; i++) 
    {
        cin >> n_lst[i];
    }

    bool confirm = false;
    int last_idx = 0;

    for (int i = 0; i < (int)n_lst.size(); i++) 
    {
        if (n_lst[i] >= 250) 
        {
            confirm = true;
            last_idx = i;  
            break;
        }
    }

    int sum_val = 0;
    double avg = 0.0;

    if (confirm) 
    {
        for (int i = 0; i < last_idx; i++) 
        {
            sum_val += n_lst[i];
        }
        avg = (last_idx == 0) ? 0.0 : static_cast<double>(sum_val) / last_idx;
    } 
    else 
    {
        for (int i = 0; i < (int)n_lst.size(); i++) 
        {
            sum_val += n_lst[i];
        }
        avg = static_cast<double>(sum_val) / n_lst.size();
    }

    cout << sum_val << " " << fixed << setprecision(1) << avg << '\n';
    return 0;
}
