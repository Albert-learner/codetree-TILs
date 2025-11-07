#include <iostream>
using namespace std;

int main() 
{
    // Please write your code here.
    int n, cnts = 1;
    cin >> n;

    for(int i = n; i > 0; i--)
    {
        for(int j = n; j > 0; j--)
        {
            if(j > i)
                cout << "  ";
            else
            {
                cout << cnts << ' ';
                cnts += 1;

                if(cnts == 10)
                    cnts = 1;
            }
        }
        cout << endl;
    }
    return 0;
}