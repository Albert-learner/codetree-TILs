#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    // Please write your code here.

    int n, n_elem;
    vector<int> n_lst, even_lst;

    cin >> n;
    for(int i = 0; i < n; i++)
    {
        cin >> n_elem;
        if(n_elem % 2 == 0)
        {
            n_lst.push_back(n_elem);
        }
    }

    if(n_lst.size() == 0)
    {
        n_lst.push_back(0);
    }
    else
    {
        reverse(n_lst.begin(), n_lst.end());
        for(int i:n_lst)
            cout << i << ' ';
    }
    
    return 0;
}