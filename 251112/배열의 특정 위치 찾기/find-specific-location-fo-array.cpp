#include <iostream>
#include <vector>
#include <iomanip>  
using namespace std;

int main() 
{
    vector<int> n_lst;
    int x;
    while (cin >> x) 
    {  
        n_lst.push_back(x);
    }

    vector<int> evals, threes;

    for (int i = 0; i < (int)n_lst.size(); i++) 
    {
        int idx = i + 1;  
        if (idx % 2 == 0)
            evals.push_back(n_lst[i]);
        if (idx % 3 == 0)
            threes.push_back(n_lst[i]);
    }

    int sum_evals = 0;
    for (int n : evals) sum_evals += n;

    double sum_threes = 0;
    for (int n : threes) sum_threes += n;

    double avg_threes = sum_threes / threes.size();

    cout << sum_evals << " " << fixed << setprecision(1) << avg_threes << '\n';

    return 0;
}
