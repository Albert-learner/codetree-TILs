#include <iostream>
using namespace std;

int main() 
{
    // Please write your code here.
    int n, cnts = 2;
    cin >> n;

    for(int i = 0; i < n; i++)
    {
        for(int j = 0; j < n; j++)
        {
            cout << cnts << ' ';
            cnts += 2;
            if(cnts > 8)
                cnts = 2;
        }
        cout << endl;          
    }
    return 0;
}