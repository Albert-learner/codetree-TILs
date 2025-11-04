#include <iostream>
using namespace std;

int main() 
{
    // Please write your code here.
    int n, cnts = 9;
    cin >> n;

    for(int i = 0; i < n; i++)
    {
        for(int j = 0; j < n; j++)
        {
            cout << cnts;
            cnts -= 1;
            if(cnts < 1)
                cnts = 9;
        }
        cout << endl;
    }
    return 0;
}