#include <iostream>
#include <vector>
using namespace std;

int main() {
    // Please write your code here.
    int num, threes = 0, fives = 0;
    vector<int> n_lst;

    for(int i = 0; i < 10; i++)
    {
        cin >> num;
        n_lst.push_back(num);
    }

    for(int i = 0; i < 10; i++)
    {
        if(n_lst[i] % 3 == 0)
            threes += 1;
        
        if(n_lst[i] % 5 == 0)
            fives += 1;
    }

    cout << threes << ' ' << fives;
    return 0;
}