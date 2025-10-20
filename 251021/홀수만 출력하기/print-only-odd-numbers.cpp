#include <iostream>
#include <vector>
using namespace std;

int main() 
{
    // Please write your code here.
    int n, cst;
    vector<int> n_lst;
    cin >> n;

    for(int i = 0; i < n; i++)
    {
        cin >> cst;
        n_lst.push_back(cst);
    }

    for(int i = 0; i < n; i++)
    {
        if(n_lst[i] % 3 == 0)
            cout << n_lst[i] << endl;
    }
    
    return 0;
}