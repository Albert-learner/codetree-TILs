#include <iostream>
#include <vector>
using namespace std;

int main() 
{
    // Please write your code here.
    int m, num;
    cin >> m;
    vector<long long> n_lst(m);

    for(int i = 0; i < m; i++)
    {
        cin >> n_lst[i];
    }

    for(long long n: n_lst)
    {
        int cnts = 0;
        while(n != 1)
        {
            if(n % 2 == 0)
                n /= 2;
            else
                n = n * 3 + 1;

            cnts++;
        }
        cout << cnts << endl;
    }

    return 0;
}