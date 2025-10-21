#include <iostream>
#include <vector>
using namespace std;

int main() 
{
    // Please write your code here.
    int cst, odds = 0;
    vector<int> ten_lst;

    for(int i = 0; i < 10; i++)
    {
        cin >> cst;
        ten_lst.push_back(cst);
    }

    for(int i = 0; i < 10; i++)
    {
        if(ten_lst[i] % 2 == 1)
            odds += 1;
    }
    cout << odds;
    return 0;
}