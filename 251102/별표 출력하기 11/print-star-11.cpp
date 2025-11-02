#include <iostream>
using namespace std;

int main() 
{
    // Please write your code here.
    int n;
    cin >> n;

    for(int i = 1; i < 2 * n + 2; i++)
    {
        for(int j = 1; j < 2 * n + 2; j++)
        {
            if(i % 2 == 1 || j % 2 == 1)
                cout << "* ";
            else
                cout << "  ";
        }
        cout << endl;
    }
    return 0;
}