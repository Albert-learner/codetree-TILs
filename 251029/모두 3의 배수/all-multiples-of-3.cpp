#include <iostream>
using namespace std;

int main() 
{
    // Please write your code here.
    int cst;
    bool check[5];
    for(int i = 0; i < 5; i++)
    {
        cin >> cst;
        if(cst % 3 == 0)
            check[i] = true;
        else
            check[i] = false;
    }

    for(int i = 0; i < 5; i++)
    {
        if(check[i] == false)
        {
            cout << 0;
            break;
        }
    }
    cout << 1;
    return 0;
}